# ADR-008: Quality Agent Architecture

**Status**: Accepted
**Date**: 2025-09-22
**Decision**: Quality Agent as parent enforcer pattern

## Context

The discovery of "test theater" (test infrastructure without actual tests) in production projects managing irreplaceable cognitive data revealed the need for quality enforcement. Two approaches were considered:

1. **Review Agent**: CI/CD integrated blocking mechanism
2. **Quality Agent**: Standalone advisory/enforcement tool

## Decision

We will implement a **Quality Agent** that serves as the parent pattern for all quality enforcement, with Review Agents as one possible output.

## Architecture

```
Quality Agent (Core)
├── Advisory Mode (v2.0)
│   └── Warnings and recommendations
├── Strict Mode (v2.1)
│   └── Local enforcement
└── Generator Mode (v2.2)
    ├── Generate Review Agent (CI/CD configs)
    ├── Generate pre-commit hooks
    └── Generate quality badges
```

## Rationale

### Why Quality Agent Wins

1. **Progressive Enhancement Philosophy**
   - Matches AGET's three-tier degradation pattern
   - Advisory → Strict → Blocking
   - Projects adopt at their own pace

2. **Educational First, Enforcement Second**
   ```bash
   aget quality check
   # Explains WHY tests matter
   # Shows risk level
   # Provides actionable fixes
   ```

3. **Platform Agnostic**
   - Works locally without CI/CD
   - Not tied to GitHub/GitLab/Bitbucket
   - Can generate platform-specific configs later

4. **Parent Pattern Advantage**
   - Quality Agent can spawn Review Agents
   - Single source of quality rules
   - Consistent standards across enforcement mechanisms

5. **Data-Driven Risk Assessment**
   - Detects if project manages data
   - Adjusts requirements based on risk
   - "Test coverage proportional to data value"

## Implementation Phases

### Phase 1: Advisory (v2.0)
```bash
aget quality check
# WARNING: Managing cognitive data with 0 tests
# Risk Level: CRITICAL
# Recommendation: Add data integrity test
```

### Phase 2: Enforcement (v2.1)
```bash
aget quality check --strict
# ERROR: Minimum quality standards not met
# - Test theater detected (infrastructure without tests)
# - Data operations untested
# Exit code: 1
```

### Phase 3: Generation (v2.2)
```bash
aget quality generate-ci --platform=github
# Created: .github/workflows/aget-quality.yml
# This Review Agent will enforce standards on PRs

aget quality generate-hooks
# Created: .git/hooks/pre-commit
# Local enforcement before commits
```

## Quality Standards

### Minimum Bar (Gate 1)
- No test theater (if test infrastructure exists, tests must exist)
- ≥1 real test if managing data
- Test coverage >0%

### Progressive Standards
```python
risk_levels = {
    "CRITICAL": "Managing data with no tests",
    "HIGH": "Test infrastructure without tests",
    "MEDIUM": "No tests but no data management",
    "LOW": "Tests present and passing"
}
```

## Not Doing

1. **Not forcing CI/CD** - Quality Agent works locally
2. **Not blocking immediately** - Advisory mode first
3. **Not platform-specific** - Universal approach
4. **Not test framework specific** - Works with pytest, unittest, etc.

## Consequences

### Positive
- Gradual adoption path
- Educational approach reduces resistance
- Single source of quality truth
- Future-proof architecture

### Negative
- More complex than pure CI/CD approach
- Requires maintenance of quality rules
- May be ignored in advisory mode

## Example Usage

```bash
# Developer runs locally
$ aget quality check
=== AGET Quality Report ===
Test Coverage:
  ✓ Test infrastructure exists
  ✗ No actual tests (possible test theater)
  ✗ No data integrity tests (RISKY)

Risk Level: CRITICAL

Critical Issues:
  ⚠️ Managing data without data integrity tests

Immediate Action Required:
  1. Write at least one data integrity test
  2. Run: aget quality explain why-tests-matter

# Later, in CI/CD (generated Review Agent)
$ cat .github/workflows/aget-quality.yml
name: AGET Quality Check
on: [pull_request]
jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: aget quality check --strict
```

## Quote

> "The Quality Agent is a teacher first, enforcer second. It explains why quality matters before demanding it."

## References

- ADR-007: Test Requirements (the "what")
- ADR-008: Quality Agent (the "how")
- User insight: "Test infrastructure without tests is theater"

---

*This ADR establishes Quality Agent as the parent pattern for all quality enforcement mechanisms.*