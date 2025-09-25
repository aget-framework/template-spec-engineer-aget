# ADR-003: Include Architecture for AGENTS.md

**Date**: 2025-09-24
**Status**: Accepted
**Deciders**: AGET v2 development team via experimental validation

## Context

During agent-music migration, we discovered that CLAUDE.md must remain a symlink to AGENTS.md (inherited standard), but projects need to preserve custom content while receiving AGET framework updates. Initial attempts to merge content programmatically revealed this is an AI task, not a deterministic one.

## Decision

Adopt an **include architecture** where:
1. AGENTS.md contains project-specific content
2. AGENTS_AGET.md contains standard AGET protocols
3. AGENTS.md includes procedural instructions to read AGENTS_AGET.md
4. CLAUDE.md remains a symlink to AGENTS.md

## Key Discovery

**Declarative includes don't work with current AI agents:**
```markdown
<!-- DOESN'T WORK -->
<!-- aget:include AGENTS_AGET.md -->
This file includes AGENTS_AGET.md for protocols.
```

**Procedural instructions DO work:**
```markdown
<!-- WORKS -->
## 🚨 INITIALIZATION PROCEDURE (REQUIRED)
**Step 1:** Check if `AGENTS_AGET.md` exists
**Step 2:** If exists, READ IT IMMEDIATELY for protocols
**Step 3:** Use protocols from AGENTS_AGET.md for commands
```

## Experimental Validation

### Test 1: Declarative Include (Failed)
- Agent saw "This includes AGENTS_AGET.md"
- Did NOT read the file
- Used fallback behaviors from memory

### Test 2: Procedural Instructions (Success)
- Agent saw "Step 1: Check if exists"
- Successfully read AGENTS_AGET.md
- Executed protocols correctly
- Worked with both Claude Code and Codex

## Consequences

### Positive
- **Clean separation**: Framework updates never touch project content
- **Version independence**: AGENTS_AGET.md can be updated independently
- **Human installable**: Simple file drop + procedural text
- **Multi-agent compatible**: Works with Claude, Codex, likely others
- **Future proof**: Easy migration to v3 and beyond

### Negative
- **Two files**: Agents must read both files
- **Procedural requirement**: Must use imperative language
- **Repetition needed**: Instructions should appear multiple times

### Neutral
- **Mental model shift**: From single-file to include pattern
- **Documentation burden**: Must be clearly explained

## Implementation Guidelines

### Required Elements in AGENTS.md

1. **Top of file**: Initialization procedure
2. **Command sections**: "First read AGENTS_AGET.md"
3. **Bottom verification**: Checklist ensuring both files read

### Language Patterns That Work

✅ **Effective**:
- "Step 1, Step 2, Step 3"
- "You MUST read"
- "READ IT IMMEDIATELY"
- "Before ANY command"
- "If not already read, read it now"

❌ **Ineffective**:
- "This includes"
- "See also"
- "Reference"
- HTML comments alone

## Migration Strategy

### For New Projects
```bash
aget init --separate  # Creates both files with proper instructions
```

### For Existing Projects
1. Create AGENTS_AGET.md with standard protocols
2. Add procedural instructions to AGENTS.md
3. Remove duplicate protocol sections
4. Test with "hey" command

## Version Compatibility

- **v2.0**: Include architecture as opt-in (--separate flag)
- **v2.1**: Make default for new projects
- **v3.0**: Mandatory architecture, single source of truth

## Related Decisions

- ADR-001: CLAUDE.md as symlink standard
- ADR-002: Agent-driven migrations

## References

- Test commits: agent-music repository (2025-09-24)
- Original discovery: agent-music migration session
- Validation: Claude Code and Codex testing

## Lessons for AI Tool Design

1. **AI agents need procedural instructions, not declarative statements**
2. **Redundancy helps**: Multiple instruction points increase compliance
3. **Step-by-step formatting**: Numbered steps trigger procedural execution
4. **Imperative language**: "MUST" works better than "should" or "includes"
5. **Explicit verification**: Checklists help ensure completion

---
*This ADR documents a critical discovery that changes how we structure agent configurations for maintainability and updates.*