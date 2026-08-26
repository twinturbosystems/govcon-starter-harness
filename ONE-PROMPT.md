# Set up the GovCon Starter Kit in your assistant

Download first:

https://github.com/twinturbosystems/govcon-starter-harness/archive/refs/heads/main.zip

Unzip it. The downloaded folder is usually named `govcon-starter-harness-main`.

Choose one path before continuing:

1. Claude Code, full-folder mode. Use an eligible Claude subscription or Anthropic Console account. Install from https://code.claude.com/docs/en/installation .
2. Codex CLI, full-folder mode. Install from https://learn.chatgpt.com/docs/codex/cli .
3. Browser chat, limited mode. It can advise and draft, but cannot operate or save the folder. Attach [BROWSER-READY.md](BROWSER-READY.md).

## Claude Code or Codex CLI

Open a terminal in the unzipped folder:

- Windows: open the folder in File Explorer, click the address bar, type `powershell`, and press Enter.
- Mac: open Terminal with Spotlight, type `cd ` including the space, drag the folder into Terminal, and press Enter.
- Linux: use Open in Terminal if available, or open Terminal, type `cd `, drag the folder in, and press Enter.

Type `claude` or `codex`. If a trust prompt appears, verify that its full path is the folder you downloaded before approving it. For every later permission prompt, read the action and path and approve only an expected action inside this folder.

Then type:

```
Start the kit
```

Claude Code reads `CLAUDE.md` and the jobs automatically. Codex reads `AGENTS.md`; the optional orientation prompt is in [browser-prompts/codex-cli.md](browser-prompts/codex-cli.md).

For later jobs, Claude Code accepts names such as `/setup-profile`. Those kit job names are not native Codex slash commands, so in Codex say `run setup-profile`, `run find-opps`, or the matching job name in plain words.

## Browser chat

Attach [BROWSER-READY.md](BROWSER-READY.md), your own `company/profile.md` if it exists, and the solicitation you want to work on. Follow the paste-ready prompt in that bundle.

A browser chat cannot read or save the downloaded folder, run `/sync` or `/backfill`, build `dashboard.html`, assemble a submission package, or submit anything. It can produce analysis, draft text, and checklists for you to copy. Anything typed or attached is sent to the provider.

## If something goes wrong

[docs/STUCK.md](docs/STUCK.md) gives one next action for each common problem.
