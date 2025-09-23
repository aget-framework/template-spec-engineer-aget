# ADR-007: Mandatory Test Requirements

**Status**: Accepted
**Date**: 2025-09-22
**Decision**: No test theater - real tests required

## Context

User scenario revealed critical issue: Test infrastructure without actual tests creates false confidence. Projects managing irreplaceable data often have zero test coverage while maintaining elaborate test runners.

## Decision

AGET v2.0 mandates actual working tests, not just test infrastructure.

## Requirements

### Gate 1 (Minimum Viable Testing)
```yaml
test_requirements:
  framework: EXISTS
  actual_tests: ≥1 per critical operation
  coverage: >0% (literally anything but zero)
  data_tests: MANDATORY if handling data
```

### Gate 2 (Pattern Testing)
```yaml
pattern_requirements:
  each_pattern: ≥1 test
  data_corruption: explicit test
  rollback: tested
```

### Gate 5 (Production Ready)
```yaml
production_requirements:
  coverage: >80% for data operations
  edge_cases: tested
  performance: benchmarked
```

## Implementation

### Every AGET Template Must Include

```python
# tests/test_example.py
def test_something_real():
    """
    This test actually runs and validates something.
    Forces developers to write test #2.
    """
    # Not a placeholder - real validation
    assert Path("AGENTS.md").exists()

def test_data_integrity():
    """Required: Test data won't corrupt"""
    if Path("data/state.json").exists():
        with open("data/state.json") as f:
            json.load(f)  # Fails if corrupted

# BAD - Test Theater
def test_placeholder():
    pass  # This is forbidden
```

### Test Coverage Proportional to Risk

```python
# High risk = High coverage
class DataOperations:
    def save_cognitive_state(self, data):
        # This MUST have tests
        pass

# Low risk = Basic coverage
class UIHelpers:
    def format_date(self, date):
        # Nice to have tests
        pass
```

## Rationale

1. **One Real Test Changes Everything**
   - Proves the framework works
   - Makes test #2 easier to write
   - Breaks the "zero test" inertia

2. **Data Loss is Unacceptable**
   - Cognitive data is irreplaceable
   - Must test data operations
   - Prevention better than recovery

3. **Truth in Advertising**
   - If `make test` exists, tests must run
   - No false confidence
   - Honest about coverage

## Consequences

### Positive
- Real confidence in test suite
- Data corruption caught early
- Clear minimum bar
- Forces good habits

### Negative
- Slightly higher initial effort
- Can't ship "framework only"
- May slow Gate 1

## Examples

### Good: Minimal but Real
```bash
$ make test
Running tests...
test_agents_file_exists ... PASSED
test_data_not_corrupted ... PASSED
2 tests, 2 passed
```

### Bad: Test Theater
```bash
$ make test
pytest tests/
No tests found
```

## Enforcement

- Gate 1 won't pass without ≥1 real test
- Pattern PR requires test with pattern
- Templates include working example test

## Quote

> "Don't ship test plumbing without water flowing through it."

---

*This ADR prevents the false confidence of test infrastructure without implementation.*