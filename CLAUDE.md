# posts

> **`AGENTS.md` and `CLAUDE.md` must be byte-identical.** Edit `AGENTS.md`,
> copy it over `CLAUDE.md`, and check with `cmp AGENTS.md CLAUDE.md`.

Public posts, served by GitHub Pages at https://jwang47.github.io/posts/.
Read `README.md` first. Each post has its own folder with the page, the data
and the scripts. Read the folder's README before you change a post.

This repository is public. Keep personal details (names of other people,
machine paths, emails, private plans) out of it.

## Agents and context files

Claude, Codex and Gemini all work here (owner, 2026-11-25). Codex and Gemini
4 Neon (Antigravity CLI `agy`) read `AGENTS.md` and `.agents/skills/`.
Claude Code reads `CLAUDE.md` and `.claude/skills/`. `AGENTS.md` is the
source; `CLAUDE.md` is a byte-identical copy. Do not add a `GEMINI.md`
(the Flutter docs' Antigravity CLI page: `agy` reads `AGENTS.md`).
Each tool's memory reaches that tool only, so write each lasting rule or
fact here or in the README.

## Rules

- **Publishing is a human call.** A merge to `main` publishes the site.
  Work on a branch, open a pull request, and get the owner's explicit yes
  for each merge.
- Some pages are built, not hand-written. A post that builds in its own
  folder (for example `china-us-ai-2026/`, `python3 build.py`) says so in
  its README: change the sources there and rebuild. Other posts are built
  from a source folder in another repository; their README names it. Never
  hand-edit a built `index.html`: the next build overwrites it. A build
  must not overwrite the post list (`index.html`, `README.md` at the
  root).
- Name each source on the page, and keep figures as the source gives them.
- Use only data that we have permission to use.
- Before you ask for a review, open the page at phone width (390 px) and
  desktop width: no console errors, no dead links, no sideways scroll.
- Review round: one reviewer that is not the author (Gemini 4 Neon when the
  review workflow can run it, else Codex GPT-6.2 Astra, else a fresh Opus
  5.5 agent). Say in the PR which model reviewed.
- Use ASD-STE100 Simplified Technical English for explanations and PR
  bodies: short sentences, active voice.
- Keep the account email out of everything you send. Commit as
  `jwang47@users.noreply.github.com` or the agent's own address.
- Never use `git stash`, and never undo a probe with `git checkout <file>`.
