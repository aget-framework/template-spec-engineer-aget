# Include Pattern Lessons Learned

**Discovery Date**: 2025-09-24
**Context**: Late discovery during v2 development while migrating agent-music

## Executive Summary

We discovered that the include pattern for AGENTS.md requires **procedural instructions** not **declarative statements** to work with AI agents. This fundamentally changes how we implement the separation of framework and project content.

## The Core Problem

- CLAUDE.md must be a symlink to AGENTS.md (inherited standard)
- Projects have custom content that must be preserved
- AGET framework needs to update without breaking custom content
- Merging is an AI task, not deterministic programming

## The Breakthrough

### What Doesn't Work ❌

```markdown
<!-- aget:include AGENTS_AGET.md -->
This file includes AGENTS_AGET.md for standard protocols.
See AGENTS_AGET.md for session management.
```

**Why it fails**: AI agents treat these as informational comments, not actionable instructions.

### What Works ✅

```markdown
## 🚨 INITIALIZATION PROCEDURE (REQUIRED)
**Step 1:** Check if `AGENTS_AGET.md` exists
**Step 2:** If exists, READ IT IMMEDIATELY for protocols
**Step 3:** Use protocols from AGENTS_AGET.md for commands
```

**Why it works**: Procedural steps trigger action-oriented behavior in AI agents.

## Key Linguistic Patterns

### Effective Trigger Words
- **Imperative verbs**: READ, CHECK, EXECUTE, USE
- **Sequential markers**: Step 1, Step 2, First, Then
- **Urgency indicators**: IMMEDIATELY, MUST, REQUIRED
- **Conditional logic**: If exists, then read

### Ineffective Patterns
- **Passive voice**: "is included", "can be found"
- **Declarative statements**: "This includes", "Contains"
- **Soft suggestions**: "See also", "Reference"
- **HTML comments alone**: Not interpreted as instructions

## Implementation Requirements

### 1. Multiple Reinforcement Points

Place instructions in THREE locations:
1. **Top of file**: Initialization procedure
2. **Before commands**: Quick reference
3. **Bottom verification**: Checklist

### 2. Explicit Procedures

```markdown
**If user says "hey":**
1. First read AGENTS_AGET.md if not already read
2. Execute Wake Up Protocol from that file
3. Add project-specific status
```

### 3. Verification Checklists

```markdown
**Before executing ANY command**, verify:
✅ AGENTS.md (this file) - Read for project config
✅ AGENTS_AGET.md - Read for standard protocols
```

## Architectural Implications

### Benefits Realized
1. **Clean separation** between framework and project
2. **Version independence** for updates
3. **Human-installable** (just drop a file)
4. **Multi-agent compatible** (Claude, Codex, others)

### Design Constraints
1. Must use procedural language
2. Need redundant instructions
3. Two-file mental model required
4. Clear documentation essential

## Testing Protocol for New Patterns

When testing if an instruction pattern works:

1. **Start fresh session** (no memory)
2. **Use minimal prompt** ("hey")
3. **Observe behavior**:
   - Does agent check for file?
   - Does agent read file?
   - Does agent use content?
4. **Test with multiple agents** (Claude, Codex, etc.)

## Broader Implications

This discovery suggests that **AI agent instructions should be written like recipes, not descriptions**:

❌ **Description**: "This configuration includes standard protocols"
✅ **Recipe**: "Step 1: Check for protocols file. Step 2: Read it."

This pattern likely applies beyond AGET to any system where AI agents need to follow multi-file configurations or complex instructions.

## Recommended Reading Order

1. This document (lessons learned)
2. ADR-003 (formal decision record)
3. Test results in agent-music commits
4. AGENTS_TEST_VARIANTS.md (experimental variants)

## Future Research Questions

1. Can we make declarative statements work with additional context?
2. Do different AI models respond to different instruction styles?
3. How many reinforcement points are optimal?
4. Can visual markers (🚨, ⚠️) improve compliance?

---
*These lessons fundamentally change how we write instructions for AI agents, moving from declarative to procedural paradigms.*