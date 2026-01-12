# Shell Integration

This directory contains shell integration examples for the Spec Engineer template.

## Overview

Shell integration enables:
- Profile-based CLI backend selection
- Environment setup for agent sessions
- Quick access to common operations

## Files

| File | Purpose |
|------|---------|
| `spec_engineer_profile.zsh` | Example zsh profile for spec engineer agents |

## Usage

### Option 1: Source directly
```bash
export AGET_AGENT_DIR="/path/to/my-agent"
source shell/spec_engineer_profile.zsh
```

### Option 2: View documentation paths
```bash
aget_info      # Display all paths
aget_docs spec # Open specification
```

## Customization

When instantiating this template:
1. Copy `spec_engineer_profile.zsh` to your instance
2. Update `AGET_AGENT_NAME` to your agent name
3. Add domain-specific helper functions

## References

- AGET Shell Orchestration: `aget/shell/aget.zsh`
- Template Spec: `specs/Spec_Engineer_SPEC.md`
- Template Vocab: `specs/Spec_Engineer_VOCABULARY.md`
- Framework Spec: `aget/specs/AGET_TEMPLATE_SPEC.md` (CAP-TPL-014)

---

*Shell integration for template-spec-engineer-aget*
