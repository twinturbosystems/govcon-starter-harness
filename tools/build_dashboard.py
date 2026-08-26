#!/usr/bin/env python3
"""Build dashboard.html from one fixed JSON file without shell interpolation."""

from __future__ import print_function

import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = ROOT / ".claude" / "skills" / "dashboard" / "dashboard.template.html"
DATA_PATH = ROOT / "dashboard-data.json"
OUTPUT_PATH = ROOT / "dashboard.html"
TOKEN = "{{DATA}}"


def encode_for_script_data(value):
    """Return JSON that cannot close its application/json script element."""
    rendered = json.dumps(value, ensure_ascii=False, indent=2)
    return (rendered.replace("&", "\\u0026")
            .replace("<", "\\u003c")
            .replace(">", "\\u003e"))


def build_dashboard(template_path, data_path, output_path):
    template = Path(template_path).read_text(encoding="utf-8")
    if template.count(TOKEN) != 1:
        raise ValueError("The dashboard template must contain exactly one data slot.")

    with Path(data_path).open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("dashboard-data.json must contain one JSON object.")

    complete = template.replace(TOKEN, encode_for_script_data(data))
    Path(output_path).write_text(complete, encoding="utf-8")


def main():
    try:
        build_dashboard(TEMPLATE_PATH, DATA_PATH, OUTPUT_PATH)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print("Dashboard was not written: " + str(exc))
        print("Next action: fix dashboard-data.json, then run this command again.")
        return 2
    print("Wrote dashboard.html from dashboard-data.json using the tested template.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
