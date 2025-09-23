# ADR-005: Gate-Based Release Strategy

## Status
Accepted

## Date
2025-09-22

## Context
The v2 PROJECT_PLAN defines 5 gates across 5 phases (~143 hours total). Originally conceived as quality checkpoints, we recognized these gates represent natural moments where working software exists and value can be delivered.

Waiting until full v2.0 completion means:
- 143 hours before agents benefit
- No real-world feedback until the end
- Higher risk of building wrong features
- Current agents (RKB, CCB) wait months for improvements

## Decision
**Implement gate-based incremental releases.**

Each gate that produces working software becomes a release:
- Gate 1 → v2.0-alpha (internal)
- Gate 2 → v2.0-beta (close collaborators)
- Gate 3 → (skip - migration only)
- Gate 4 → v2.0-rc (first external users)
- Gate 5 → v2.0 (public)

## Consequences

### Positive
- **Immediate value**: RKB agent gets protection after Gate 1 (~19 hours)
- **Real feedback**: Each release informs next phase
- **Risk reduction**: Issues found early, not after 143 hours
- **Natural versioning**: Gates already have success criteria
- **Motivation**: Shipping working software maintains momentum

### Negative
- **Release overhead**: Each gate needs release notes, tagging
- **Compatibility burden**: Alpha/beta users need migration path
- **Expectation management**: Must clarify alpha/beta status

## Implementation

### Release Criteria
A gate becomes a release when:
1. Working commands exist (not just infrastructure)
2. Value can be delivered to current agents
3. Success criteria are met
4. Tests pass

### Version Naming
```
v2.0-alpha.1  (Gate 1)
v2.0-alpha.2  (fixes)
v2.0-beta.1   (Gate 2)
v2.0-rc.1     (Gate 4)
v2.0          (Gate 5)
```

### Distribution Strategy
- **Alpha**: Internal use only (aget-cli-agent-template, CCB, RKB)
- **Beta**: Close collaborators with warning
- **RC**: First external users with feedback request
- **Final**: Public announcement

## Example Impact

After Gate 1 (19 hours):
```bash
# RKB agent immediately benefits
aget init --project RKB
aget validate  # Ensures configuration safe

# If something breaks
aget rollback  # RKB data protected
```

## Flexibility Preserved
- Not every gate must release
- Can add fix releases between gates
- Can combine gates if moving fast
- Gate criteria remain unchanged

## References
- PROJECT_PLAN.md: Gate definitions
- SPRINT-001-GATE1.md: First sprint commitment
- ADR-003: Charter commitment (timeline flexible, scope not)

## Quote
"The constraint that frees: Having release points forces us to ship working software, not perfect software."

---

*This decision transforms gates from checkpoints into value delivery moments.*