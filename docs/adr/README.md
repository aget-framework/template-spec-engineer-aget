# Architectural Decision Records

This directory contains ADRs (Architectural Decision Records) for the AGET project, documenting significant architectural decisions and their rationale.

## Active ADRs

| ADR | Title | Status | Category | Date |
|-----|-------|--------|----------|------|
| [ADR-001](ADR-001-AGET-SCOPE-BOUNDARIES.md) | AGET Scope Boundaries | Accepted | Scope | 2025-09-22 |

## How to Use ADRs

### For Contributors
Before proposing significant changes:
1. Check existing ADRs for related decisions
2. Ensure your proposal doesn't conflict with accepted ADRs
3. Create a new ADR if your change is architecturally significant

### For CLI Agents
When users propose changes:
1. Check this directory for existing decisions
2. Reference relevant ADRs in responses
3. Suggest creating new ADRs for significant proposals

### Creating a New ADR
1. Copy `template.md` to `ADR-NNN-SHORT-TITLE.md`
2. Use sequential numbering (ADR-002, ADR-003, etc.)
3. Follow the template structure
4. Submit for review before marking as Accepted

## ADR Status Definitions

- **Draft**: Being written, not ready for review
- **Proposed**: Ready for review and discussion
- **Accepted**: Approved and in effect
- **Rejected**: Not approved, kept for reference
- **Deprecated**: No longer valid but kept for history
- **Superseded**: Replaced by another ADR (must reference the new one)

## Categories

- **Scope**: Boundaries and mission decisions
- **Architecture**: System structure decisions
- **Security**: Security-related decisions
- **Performance**: Performance trade-offs
- **Design**: Design pattern choices

## Template

See [template.md](template.md) for creating new ADRs.

## References

- [Michael Nygard's Original ADR Article](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
- [ADR GitHub Organization](https://adr.github.io)
- [AGET ADR Pattern Documentation](../../patterns/adr/README.md)