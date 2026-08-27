#!/usr/bin/env python3
"""Apply one reviewed organisation plan without putting paths in a shell command."""

from __future__ import print_function

import json
from pathlib import Path, PurePosixPath
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PLAN_PATH = ROOT / "organise-plan.json"
PROTECTED_PREFIXES = {
    ".claude", ".git", ".github", "browser-prompts", "data", "docs", "tests", "tools"
}
PROTECTED_ROOT_FILES = {
    ".gitignore", "AGENTS.md", "BROWSER-READY.md", "CLAUDE.md", "LICENSE",
    "ONE-PROMPT.md", "README.md", "SECURITY.md", "dashboard-data.json",
    "dashboard.html", "organise-plan.json"
}
PROTECTED_FILES = {
    "company/.env.local.example", "company/profile.example.md",
    "company/profile.template.md", "data/README.md", "pipeline/README.md",
    "pipeline/opportunity.template.md", "proposals/README.md"
}
INVALID_COMPONENT = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
WINDOWS_DEVICE = re.compile(
    r"^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\..*)?$", re.IGNORECASE)


class PlanError(ValueError):
    pass


def relative_path(value):
    if not isinstance(value, str) or not value.strip():
        raise PlanError("Every path must be a non-empty string.")
    normalized = value.replace("\\", "/")
    pure = PurePosixPath(normalized)
    if pure.is_absolute() or any(part in ("", ".", "..") for part in pure.parts):
        raise PlanError("Paths must stay relative to the kit folder: " + value)
    candidate = (ROOT / Path(*pure.parts)).resolve(strict=False)
    try:
        candidate.relative_to(ROOT.resolve())
    except ValueError:
        raise PlanError("Path leaves the kit folder: " + value)
    return pure, candidate


def safe_component(component):
    return (bool(component) and len(component) <= 120 and
            not INVALID_COMPONENT.search(component) and
            not component.endswith((".", " ")) and
            not WINDOWS_DEVICE.match(component))


def protect_source(pure):
    rendered = pure.as_posix()
    rendered_key = rendered.casefold()
    if pure.parts[0].casefold() in {value.casefold() for value in PROTECTED_PREFIXES}:
        raise PlanError("The plan may not move a protected kit path: " + rendered)
    if (rendered_key in {value.casefold() for value in PROTECTED_ROOT_FILES} or
            rendered_key in {value.casefold() for value in PROTECTED_FILES}):
        raise PlanError("The plan may not move a protected kit file: " + rendered)
    if rendered_key in {"data/sam.db", "company/.env.local"}:
        raise PlanError("The plan may not move protected local state: " + rendered)


def validate_destination(pure):
    parts = pure.parts
    rendered = pure.as_posix()
    rendered_key = rendered.casefold()
    protected_keys = {value.casefold() for value in PROTECTED_FILES}
    if rendered_key == "company/profile.md":
        return
    if (len(parts) == 2 and parts[0].casefold() == "pipeline" and
            parts[1].casefold().endswith(".md")):
        if rendered_key not in protected_keys and safe_component(parts[1]):
            return
    if len(parts) >= 2 and parts[0].casefold() == "proposals":
        if rendered_key not in protected_keys and all(
                safe_component(part) for part in parts[1:]):
            return
    raise PlanError("Destination is outside the allowed company, pipeline, or proposals layout: " + rendered)


def validate_directory(pure):
    if pure.as_posix().casefold() in {"company", "pipeline", "proposals", "data"}:
        return
    if len(pure.parts) >= 2 and pure.parts[0].casefold() == "proposals" and all(
            safe_component(part) for part in pure.parts[1:]):
        return
    raise PlanError("Directory is outside the allowed layout: " + pure.as_posix())


def load_and_validate(plan_path=PLAN_PATH):
    with Path(plan_path).open("r", encoding="utf-8") as handle:
        plan = json.load(handle)
    if not isinstance(plan, dict):
        raise PlanError("organise-plan.json must contain one JSON object.")
    if set(plan) - {"directories", "moves"}:
        raise PlanError("The plan may contain only directories and moves.")
    directories = plan.get("directories", [])
    moves = plan.get("moves", [])
    if not isinstance(directories, list) or not isinstance(moves, list):
        raise PlanError("directories and moves must be JSON lists.")

    checked_directories = []
    directory_paths = set()
    for value in directories:
        pure, path = relative_path(value)
        validate_directory(pure)
        if path.exists() and not path.is_dir():
            raise PlanError("A file blocks the planned directory: " + pure.as_posix())
        if path in directory_paths:
            raise PlanError("The plan repeats a directory: " + pure.as_posix())
        directory_paths.add(path)
        checked_directories.append((pure, path))

    for pure, path in checked_directories:
        if not path.parent.is_dir() and path.parent not in directory_paths:
            raise PlanError("The plan omits the parent directory for: " + pure.as_posix())

    checked_moves = []
    sources = set()
    destinations = set()
    for item in moves:
        if not isinstance(item, dict) or set(item) != {"source", "destination"}:
            raise PlanError("Every move needs only source and destination.")
        source_pure, source = relative_path(item["source"])
        destination_pure, destination = relative_path(item["destination"])
        protect_source(source_pure)
        validate_destination(destination_pure)
        if not source.exists():
            raise PlanError("Source does not exist: " + source_pure.as_posix())
        if source.is_symlink():
            raise PlanError("Symlinks are left alone: " + source_pure.as_posix())
        if source.is_dir() and not (
                len(source_pure.parts) == 2 and
                source_pure.parts[0].casefold() == "proposals"):
            raise PlanError("Only a direct proposal folder may be moved as a folder: " +
                            source_pure.as_posix())
        if source.is_file() and not (
                (len(source_pure.parts) == 1 and source_pure.suffix.lower() == ".md") or
                source_pure.parts[0].casefold() in {"company", "pipeline", "proposals"}):
            raise PlanError("Source is outside the user-work paths: " +
                            source_pure.as_posix())
        if destination.exists():
            raise PlanError("Destination already exists: " + destination_pure.as_posix())
        if destination in directory_paths:
            raise PlanError("A move destination is also a planned directory: " +
                            destination_pure.as_posix())
        if not destination.parent.is_dir() and destination.parent not in directory_paths:
            raise PlanError("The plan omits the destination folder: " +
                            destination_pure.parent.as_posix())
        if source == destination:
            raise PlanError("Source and destination are the same: " + source_pure.as_posix())
        if source in sources or destination in destinations:
            raise PlanError("The plan repeats a source or destination.")
        sources.add(source)
        destinations.add(destination)
        checked_moves.append((source_pure, source, destination_pure, destination))

    for _, source, _, _ in checked_moves:
        for _, other, _, _ in checked_moves:
            if source != other and source in other.parents:
                raise PlanError("The plan may not move a folder and something inside it together.")
        for _, _, destination_pure, destination in checked_moves:
            if source != destination and source in destination.parents:
                raise PlanError("A destination may not sit inside a folder that the plan moves: " +
                                destination_pure.as_posix())
    return checked_directories, checked_moves


def apply_plan(plan_path=PLAN_PATH):
    directories, moves = load_and_validate(plan_path)
    for _, path in sorted(directories, key=lambda item: len(item[0].parts)):
        path.mkdir(exist_ok=True)
    for source_pure, source, destination_pure, destination in moves:
        if not destination.parent.is_dir():
            raise PlanError("Destination folder is missing: " + destination_pure.parent.as_posix())
        if destination.exists():
            raise PlanError("Destination appeared after review: " + destination_pure.as_posix())
        source.rename(destination)
        print("Moved %s to %s" % (source_pure.as_posix(), destination_pure.as_posix()))
    print("Directory entries processed: %d; items moved: %d." %
          (len(directories), len(moves)))


def main():
    try:
        apply_plan()
    except (OSError, PlanError, json.JSONDecodeError) as exc:
        print("Stopped before any further change: " + str(exc))
        print("Next action: review organise-plan.json and resolve the reported path or collision.")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
