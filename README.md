# Preflights

Code fast with AI — without giving up architectural clarity.

Preflights is a lightweight CLI tool that helps developers clarify decisions before letting an AI agent write code.
It turns a vague intention into explicit decisions and a clear execution brief — without slowing you down.

---

## What is Preflights?

Preflights sits before AI coding agents (Claude Code, Cursor, Windsurf).
It does not generate code.
It forces clarification, captures decisions, and produces a clear brief so AI agents can implement without guessing.

Think of it as a pre-flight checklist for AI-assisted development.

---

## Why Preflights exists

AI coding tools are incredibly fast.
The real problem is not speed — it's everything that gets decided implicitly:
- architectural choices made by accident
- inconsistencies across files
- rework disguised as "fast iteration"
- technical debt with no paper trail

With vibe coding, you often have to choose:
- move fast
- or keep quality and clarity

Preflights removes that trade-off.

You can keep the vibe — while making decisions explicit, traceable, and reversible.

---

## Quickstart

From the root of a git repository:

```bash
pf start "Add user authentication"
```

Or with uvx (no install needed):

```bash
uvx preflights start "Add user authentication"
```

Preflights will:
- ask a few targeted questions
- clarify what needs to be decided vs implemented
- generate clear artifacts for your AI agent

That's it.

---

## Installation

```bash
pip install preflights
pf start "Add authentication"
```

Or with uvx (no install needed):

```bash
uvx preflights start "Add authentication"
```

### From source (contributors)

```bash
git clone https://github.com/ptngaye/preflights.git
cd preflights
pip install -e .
```

---

## Usage — the Golden Path

1. **Run Preflights** from a git repository

```bash
pf start "Add OAuth authentication"
```

2. **Answer the clarification questions** (interactive by default, one flow)

3. **Preflights generates documentation** in `docs/`
   - `docs/CURRENT_TASK.md` — always created
   - `docs/adr/{UID}_{slug}.md` — if a structural decision was made
   - `docs/ARCHITECTURE_STATE.md` — regenerated when ADR is created/updated

   Previous tasks are archived in `docs/archive/task/`.

4. **Open your AI coding tool** and tell it to implement strictly based on `CURRENT_TASK.md`

Preflights stops here.
The AI agent implements.
No decisions happen during coding.

**Session state** is stored in `.preflights/` (auto-gitignored).

---

## What files are generated?

Preflights uses three explicit artifacts.

### ADR — Architecture Decision Records

Long-term, structural decisions:
- frameworks
- auth strategy
- database choices

They are immutable, ordered, and versioned.

You don't rewrite history — you supersede it.

---

### CURRENT_TASK.md

The only thing your AI agent should implement right now.

It contains:
- goal
- context
- allowed files
- forbidden files
- acceptance criteria

If it's not in CURRENT_TASK.md, it shouldn't be implemented.

---

### ARCHITECTURE_STATE.md

A generated snapshot of the current architecture.
- compact
- machine-readable
- fast to scan
- never edited manually

It exists to give agents context — not to replace ADRs.

Only regenerated when an ADR is created or updated.

---

## Core concepts (human version)

- Decisions are durable → ADR
- Intentions are local → TASK
- Code is disposable → implementation

If changing something would require migration or refactoring many files:
it's probably a decision.

Otherwise:
it's just a task.

---

## Architecture (very short)

Preflights follows a strict Ports & Adapters design:
- Core — pure, deterministic, no I/O
- Application — orchestration
- Adapters — filesystem, LLM, clock, IDs
- CLI — human interface (golden path)
- MCP — fallback integration for agents

The Core never touches the filesystem or an LLM.

---

## Development & Contributing

Requirements:
- Python 3.11+
- git

Run tests:

```bash
pytest
```

Type checking:

```bash
mypy preflights/
```

Full validation:

```bash
pytest && mypy preflights/
```

Core rules:
- no I/O
- no randomness
- same input → same output
- dataclasses are frozen
- no Any types

See `AGENTS.md` for agent-specific instructions.

---

## License

Apache License 2.0

You can use, modify, and distribute Preflights freely —
including for commercial projects — without lock-in.

---

Preflights is not here to slow you down.
It's here to make sure speed doesn't silently destroy quality.
