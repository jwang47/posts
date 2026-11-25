# posts

> **`AGENTS.md` and `CLAUDE.md` must be byte-identical.** Edit one, copy it
> over the other, and check with `cmp AGENTS.md CLAUDE.md`.
> `GEMINI.md` imports this file (`@./AGENTS.md`) for Gemini, so Claude,
> Codex and Gemini read the same rules. Keep every rule here, not there.

Public posts, served by GitHub Pages. Each post has its own folder with the
page, the data and the scripts. Read `README.md` first. Claude, Codex and
Gemini all work here, so durable facts live in this repository, not in agent
memory.

## Rules

- **This repository is public.** A push to `main` publishes the post. Get
  explicit human confirmation before every merge or push to `main` and
  before any change to the Pages settings. State the exact action and
  target.
- Keep personal details out: no names of other people, emails, machine
  paths or private trip details that the post does not need.
- Pages are plain HTML with no build step. Each post names its sources and
  links them. Use only data that we have permission to use.
- When a post is published, add it to the table in `README.md` and to
  `index.html`.
- Work on a branch and open a pull request. Say in the PR how you checked
  the page (for example, a phone and a desktop screenshot).
- **Reviewer order** (Jiahua, 2026-11-25): Gemini 4 Neon is the preferred
  reviewer, but no review round can run it yet. Until one exists, a fresh
  Opus 5.5 agent (not the author) reviews, and Fable 5.2 only a high-risk
  change. Say in the PR which model
  reviewed.
- Never ask a human to paste a secret into a chat or a PR. Keep the account
  email out of everything you send. Commit as
  `jwang47@users.noreply.github.com` or the agent's own address.
- Use ASD-STE100 Simplified Technical English for explanations and PR
  bodies: short sentences, active voice.
- Never use `git stash`, and never undo a probe with `git checkout <file>`.
