# Architecture Decision Records

## Context and Publication Notice

These are decision records for AGET v2.0 development. They capture decisions at a point in time and may evolve. Not all decisions will make it to production.

**Publication Commitment**: These ADRs are public to share learnings with the community. However:
- They represent decisions, not promises
- Context and constraints may differ for your project
- Status markers indicate maturity (Proposed → Accepted → Deprecated)
- All content has been sanitized to protect private information

## Active ADRs

| ADR | Title | Status | Public Value | Date |
|-----|-------|--------|--------------|------|
| [ADR-001](ADR-001-VERSIONING-STRATEGY.md) | Versioning Strategy | Accepted | High | 2025-09-22 |
| [ADR-002](ADR-002-PYTHON-IMPLEMENTATION.md) | Python Implementation | Accepted | Medium | 2025-09-22 |
| [ADR-003](ADR-003-V2-CHARTER.md) | V2 Charter Commitment | Accepted | High | 2025-09-22 |
| [ADR-004](ADR-004-THREE-TIER-DEGRADATION.md) | Three-Tier Degradation | Accepted | **Very High** | 2025-09-22 |
| [ADR-005](ADR-005-GATE-BASED-RELEASES.md) | Gate-Based Releases | Accepted | High | 2025-09-22 |
| [ADR-006](ADR-006-REPO-SEPARATION-STRATEGY.md) | Repository Separation | Proposed | High | 2025-09-22 |
| [ADR-007](ADR-007-TEST-REQUIREMENTS.md) | Test Requirements | Accepted | **Very High** | 2025-09-22 |
| [ADR-008](ADR-008-QUALITY-AGENT-ARCHITECTURE.md) | Quality Agent | Accepted | **Very High** | 2025-09-22 |

## Key Patterns Worth Sharing

### Three-Tier Degradation (ADR-004)
Every feature works in three modes: Rich (with tools) → Standard (basic tools) → Basic (guaranteed). Ensures universal compatibility.

### No Test Theater (ADR-007)
Test infrastructure without tests is dangerous. If `make test` exists, actual tests must run. Coverage proportional to data value.

### Quality Agent (ADR-008)
Quality enforcement that educates before enforcing. Progressive: Advisory → Strict → Blocking. Parent pattern for CI/CD configs.

## Privacy and Sanitization Policy

All ADRs have been sanitized to:
- Remove references to private repositories
- Use generic examples only
- Focus on patterns over specifics
- Protect PII and private project details

## How to Use These ADRs

### For Learning
- Read ADRs marked "Very High" public value first
- Consider your context and constraints
- Adapt patterns to your needs

### For Contributing
- Propose new ADRs via PR
- Include: Context, Decision, Rationale, Consequences
- Sanitize any private information
- Mark status as "Proposed" initially

### For Implementation
- Check ADR status before implementing
- "Accepted" ADRs are active decisions
- "Deprecated" ADRs include migration notes

## ADR Status Definitions

- **Proposed**: Ready for review and discussion
- **Accepted**: Approved and in effect
- **Deprecated**: No longer valid but kept for history
- **Superseded**: Replaced by another ADR

## Living Documentation

These ADRs are living documents:
- Updated as decisions evolve
- New ADRs added as needed
- Community feedback incorporated
- Status tracked transparently

## Citation

If you use these patterns, attribution is appreciated:
```
AGET Architecture Decisions
https://github.com/aget-cli-agent-template/docs/adr
```

## References

- [Michael Nygard's ADR Article](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
- [ADR GitHub Organization](https://adr.github.io)

---

*Last Updated: 2025-09-22*
*Next Review: After Gate 2 (v2.0-beta)*