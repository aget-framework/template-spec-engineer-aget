# ADR-001: AGET Scope Boundaries

**Date**: 2025-09-22
**Status**: Accepted
**Deciders**: Gabor Melli, AGET Community
**Category**: Scope
**Confidence**: High

## Context

During AGET development and adoption, proposals arise for features that could benefit many projects but may not align with AGET's core mission. A specific case emerged when a comprehensive Unified Tracking Database specification was proposed as an AGET pattern (EP-13).

The proposal included:
- Database schema consolidation (7+ databases → 1)
- Thread-safe implementation with connection pooling
- Migration strategies with backward compatibility adapters
- Detailed implementation specifications

While well-designed and following AGET patterns, this raised fundamental questions:
- What belongs in AGET core?
- Where are the boundaries?
- How do we prevent scope creep?
- What is AGET's essential purpose?

## Decision

**AGET remains strictly focused on the conversation layer between CLI agents and codebases. Implementation patterns, architectural decisions, and domain-specific solutions belong in individual projects, not AGET core.**

The litmus test for any AGET feature:
1. **"Is this about HOW agents talk to projects?"** → ✅ Consider for AGET
2. **"Is this about WHAT projects do internally?"** → ❌ Belongs in the project

## Consequences

### Positive
- **Maintained simplicity**: AGET remains lightweight and easy to adopt
- **Clear boundaries**: Prevents feature creep and framework bloat
- **Universal applicability**: Works with any project, any language, any framework
- **Focused mission**: Excellence in one thing rather than mediocrity in many
- **Quick adoption**: Installation remains under 5 minutes
- **Zero lock-in**: Projects maintain architectural freedom

### Negative
- **Excluded useful patterns**: Some beneficial patterns won't be included
- **Duplication possible**: Projects may solve similar problems independently
- **Limited guidance**: AGET won't provide implementation advice

### Neutral
- **Clear separation**: Projects handle their implementation, AGET handles conversation
- **Extension possible**: Projects can create their own pattern libraries

## Alternatives Considered

### Option 1: Include Implementation Patterns
- **Description**: Accept database, API, and architecture patterns into AGET
- **Pros**: More comprehensive solution, reduces duplication
- **Cons**: Scope creep, increased complexity, lost focus
- **Reason for rejection**: Violates AGET's core mission of being a conversation layer

### Option 2: Create AGET Extensions
- **Description**: Separate repositories for different pattern types
- **Pros**: Modular approach, optional adoption
- **Cons**: Fragmentation, maintenance burden, confusion
- **Reason for rejection**: Still implies AGET ownership of implementation concerns

### Option 3: Community Pattern Library
- **Description**: Curated but not included collection of patterns
- **Pros**: Best of both worlds, community-driven
- **Cons**: Quality control, versioning challenges
- **Reason for rejection**: Could be future enhancement, but not core responsibility

## Implementation Notes

1. Document this philosophy in PHILOSOPHY.md
2. Reference in CONTRIBUTING.md for contributors
3. Use as precedent for enhancement proposal reviews
4. Create clear examples of what belongs vs. what doesn't

## Review Triggers

This decision should be reviewed if:
- AGET's core mission fundamentally changes
- Overwhelming community demand for implementation patterns (>80% of users)
- A clean separation mechanism is developed that maintains simplicity
- Competing solutions fragment the ecosystem

## References

- Original proposal: Unified Tracking Database specification (EP-13)
- AGET mission statement: "Making codebases CLI agent-ready"
- Philosophy: "AGET enables conversations about work, not the work itself"
- Related: docs/PHILOSOPHY.md (to be created)

## Notes

This is AGET's first ADR, establishing the pattern and the fundamental scope boundary. It serves as both a decision record and a precedent for how future boundary questions should be evaluated.

The database consolidation pattern that triggered this decision is an excellent solution—for the specific project that needs it. It demonstrates the type of implementation detail that projects should handle independently while using AGET to make those implementations conversable with CLI agents.