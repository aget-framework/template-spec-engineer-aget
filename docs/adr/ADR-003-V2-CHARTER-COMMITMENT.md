# ADR-003: AGET v2 Charter Commitment

**Date**: 2025-09-22
**Status**: Accepted
**Deciders**: Gabor Melli
**Category**: Product Strategy
**Confidence**: High

## Context

AGET v1 established the technical foundation but revealed critical usability gaps:
- High friction for new users
- Trial-and-error configuration process
- No safety mechanisms (preview/undo)
- Scattered state files

v2 represents a commitment to transform AGET from a template collection to a practical tool that developers want to use daily.

## Decision

**Commit to AGET v2 Charter with fixed scope and flexible timeline.**

Core commitment: Deliver every feature in the charter's "Core Commands" and meet all "Hard Requirements" before release.

## Charter Summary

**Mission**: Help individual developers configure AI coding agents through simple, local, file-based patterns.

**Core Promise**: Transform agent configuration from trial-and-error to predictable patterns in under 60 seconds.

**Scope Commitment** (~120 hours):
- Phase 1: Core CLI (~40 hours)
- Phase 2: Patterns Library with business rules (~35 hours)
- Phase 3: Polish (~20 hours)
- Phase 4: Documentation (~10 hours)
- Phase 5: Testing & Validation (~15 hours)

## Success Criteria

### Release Gates (Must Pass)
- [ ] Time to working config: <60 seconds
- [ ] All commands complete in <2 seconds
- [ ] Zero runtime dependencies beyond Python 3.8+
- [ ] Backward compatible with v1 AGENTS.md
- [ ] All tests passing on Mac/Linux/Windows
- [ ] First 5 users successfully onboard without help

### Quality Metrics (Measure)
- 80% of users never need documentation
- <5% rollback rate after applying patterns
- User satisfaction >7/10 from first 10 users

## Consequences

### Positive
- Clear, achievable scope prevents drift
- Focus on individual developers (not enterprises)
- Testable success criteria
- Quality gates ensure good first impression

### Negative
- No agent coordination features (originally discussed)
- Limited to local operation (no cloud)
- Longer timeline due to testing requirements

## Implementation Tracking

Progress tracked in:
- `/docs/V2_CHARTER.md` - Full charter document
- `/docs/V2_PROGRESS.md` - Implementation status
- `/tests/v2_acceptance/` - Acceptance criteria tests

## Review Triggers

Re-evaluate if:
- First 5 users cannot onboard successfully
- Core commands take >2 seconds consistently
- Scope additions requested before Phase 5 complete

## References

- V2 Charter Document (2025-09-22)
- Best Practices Analysis Session
- User feedback from v1 deployment

## The Commitment Statement

"We commit to delivering every feature in the Core Commands section of the v2 Charter, meeting all Hard Requirements, and ensuring the first few users have a positive experience. Timeline is flexible; scope and quality are not."

---
*This ADR records the formal commitment to v2's scope and success criteria.*