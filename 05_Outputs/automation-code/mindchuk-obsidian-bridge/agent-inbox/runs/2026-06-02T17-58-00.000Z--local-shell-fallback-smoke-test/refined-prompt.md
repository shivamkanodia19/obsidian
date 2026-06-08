Work in the Obsidian vault on Windows and use `C:\Users\shiva\obsidian\05_Outputs\automation-code\mindchuk-obsidian-bridge\agent-inbox\runs\2026-06-02T17-58-00.000Z--local-shell-fallback-smoke-test` as the only writable directory.

Set the shell command working directory to that run directory. Run exactly one PowerShell shell command, and it must only print the current working directory, for example `(Get-Location).Path`. Capture the exact printed path from that one command. Do not run any other shell commands.

After that, create `success-note.md` inside the run directory. Its contents must include:
`PASS`
the exact printed working directory path on its own line
one short sentence confirming the fallback pipeline works

Do not modify any files outside the run directory. If you cannot complete the task without running additional shell commands or if the path/output is ambiguous, create `blocker-note.md` in the run directory explaining the blocker instead of guessing.
