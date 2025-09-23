# ADR-006: Repository Separation Strategy

**Status**: Proposed
**Date**: 2025-09-22
**Decision**: Start simple, separate when needed

## Context

The question arose about AGET's vision for repository structure, specifically whether projects should use multiple repositories (CCB, CCB-data, CCB-context, CCB-workspace) by default.

## Decision

AGET recommends starting with a single repository and separating concerns only when specific needs arise.

## Default Structure (Single Repo)

```
project/
├── .aget/          # Metadata (gitignore sensitive parts)
├── AGENTS.md       # Agent configuration
├── patterns/       # Reusable patterns
├── data/          # Agent memory/state (gitignore if sensitive)
├── workspace/     # Active work area
└── src/           # Your actual code
```

## When to Separate

Consider repository separation when you have:

1. **Sensitive Data** (`project-data/`)
   - Personal cognitive metrics
   - API keys or credentials
   - Private session logs
   - User-specific state

2. **Large Binary Assets** (`project-assets/`)
   - Training data
   - Model weights
   - Generated artifacts
   - Media files

3. **Shared Patterns** (`project-patterns/`)
   - Patterns used across multiple projects
   - Community contributions
   - Organization-wide standards

## Migration Path

```bash
# Start simple
aget init  # Creates everything in current repo

# Later, if needed
aget separate --data  # Moves data/ to ../project-data/
aget separate --patterns  # Moves patterns/ to ../project-patterns/
```

## Rationale

1. **Simplicity First**: Most projects don't need multiple repos
2. **Progressive Complexity**: Add separation when pain points emerge
3. **Atomic Operations**: Single repo = simpler commits, rollbacks
4. **Lower Barrier**: Easier onboarding for new users
5. **Real Usage**: Dogfooding shows single repo works fine

## Consequences

### Positive
- Simpler mental model
- Easier version control
- Faster development
- Clear migration path

### Negative
- May need refactoring later
- Initial structure might mix concerns
- Requires discipline about .gitignore

## Examples

### Simple Project (Default)
```
my-tool/           # Everything in one place
├── .aget/
├── AGENTS.md
└── main.py
```

### Sensitive Project (Separated)
```
project/           # Public code
├── .aget/
└── AGENTS.md

project-data/      # Private data (separate repo)
├── metrics/
└── state/
```

## Not Doing

- Not enforcing multiple repos by default
- Not creating complex symlink structures
- Not requiring submodules for basic usage

---

*Note: This aligns with AGET's three-tier degradation pattern - start at the basic tier (single repo) and upgrade to richer tiers (multiple repos) only when beneficial.*