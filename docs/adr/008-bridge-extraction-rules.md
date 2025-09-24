# ADR-008: Bridge Extraction Rules

**Date**: 2025-09-24
**Status**: Proposed
**Context**: Formalize the bridge mechanism for extracting public value from private work

## Decision

Establish standard rules and automation for the bridge extraction process that transforms private agent explorations (outputs/) into public tools (Outputs/).

## Context

The manual bridge extraction in llm-manager-aget proved the concept works but revealed the need for:
1. Clear rules about what to remove/preserve
2. Automation to reduce friction
3. Consistent documentation generation
4. Tracking of extractions

## Extraction Rules Engine

### Data Sanitization Rules

#### Must Remove
```python
MUST_REMOVE = [
    # Credentials
    r'api[_-]?key\s*=\s*["\'].*["\']',
    r'token\s*=\s*["\'].*["\']',
    r'password\s*=\s*["\'].*["\']',
    r'secret\s*=\s*["\'].*["\']',

    # Personal/Org Data
    r'email\s*=\s*["\'][^"\']+@[^"\']+["\']',
    r'company\s*=\s*["\'].*["\']',

    # File Paths (absolute)
    r'/Users/[^/\s]+',
    r'/home/[^/\s]+',
    r'C:\\Users\\[^\\s]+',

    # Internal URLs
    r'https?://internal\.',
    r'https?://localhost',
    r'https?://127\.0\.0\.1'
]
```

#### Should Simplify
```python
SIMPLIFY = [
    # Complex internal APIs → Simple public interface
    "Multiple internal methods → Single public method",
    "Private state management → Stateless functions",
    "Internal caching → Optional caching",
    "Complex error handling → Basic try/catch",
    "Internal logging → Optional logging"
]
```

#### Must Preserve
```python
PRESERVE = [
    "Core algorithms",
    "Business logic",
    "Data structures",
    "Public API signatures",
    "License headers",
    "Attribution comments"
]
```

### Transformation Pipeline

```python
def bridge_extract(source_path: Path, target_path: Path) -> Dict:
    """
    Extract public tool from private implementation.
    """
    pipeline = [
        scan_source,           # Identify extractable components
        remove_sensitive,      # Strip credentials and private data
        simplify_interface,    # Create cleaner public API
        generate_docs,         # Create README and docstrings
        create_package,        # Generate setup.py
        validate_extraction,   # Ensure it works standalone
        document_evolution     # Track the extraction
    ]

    result = source_path
    for step in pipeline:
        result = step(result, target_path)

    return result
```

### Extraction Types

#### 1. Full Tool Extraction
Complete standalone tool from agent module:
```bash
aget extract --type tool \
    --from src/cost_optimizer.py \
    --to Outputs/llm-cost-analyzer \
    --standalone
```

#### 2. Pattern Extraction
Reusable pattern from exploration:
```bash
aget extract --type pattern \
    --from outputs/experiments/caching_strategy.py \
    --to patterns/optimization/cache.py
```

#### 3. Library Extraction
Utility library from agent helpers:
```bash
aget extract --type library \
    --from src/utils/ \
    --to Outputs/agent-utils \
    --package
```

#### 4. Documentation Extraction
Knowledge from explorations:
```bash
aget extract --type docs \
    --from outputs/analysis/ \
    --to Outputs/analysis-guide \
    --format markdown
```

## Automation Features

### Auto-Detection
```bash
# Scan for extractable components
aget extract --auto

Detected extractable components:
1. src/llm_tracker.py → Cost tracking library
2. outputs/analysis/optimization.py → Optimization patterns
3. data/benchmarks/ → Benchmark dataset

Select items to extract (1,2,3 or all):
```

### Metadata Generation

Each extraction creates:

**Outputs/tool-name/EXTRACTION.md**:
```markdown
# Extraction Metadata

- **Source**: src/cost_optimizer.py
- **Extracted**: 2025-09-24T10:30:00
- **Type**: tool
- **Agent**: llm-manager-aget
- **Version**: 1.0.0

## Transformations Applied
- Removed API key references (3 instances)
- Simplified error handling
- Extracted pricing data to separate module
- Generated setup.py for pip installation

## Dependencies
- None (made standalone)

## Testing
- ✅ Import test passed
- ✅ Basic functionality verified
- ✅ No sensitive data found
```

### Documentation Generation

Auto-generates from docstrings and analysis:

1. **README.md** - From module docstring + examples
2. **setup.py** - From imports and metadata
3. **LICENSE** - Inherited from source project
4. **examples.py** - From test cases
5. **CHANGELOG.md** - From evolution tracking

## Validation Rules

Before extraction is complete:

```python
VALIDATION_CHECKS = [
    "no_secrets",        # No API keys or credentials
    "imports_work",      # Can be imported standalone
    "has_docs",          # README exists and is complete
    "has_examples",      # At least one working example
    "no_internal_refs",  # No references to private code
    "passes_tests"       # Basic smoke tests pass
]
```

## Evolution Tracking

Each extraction logged in `.aget/evolution/`:

**extraction_20250924_103000.md**:
```markdown
# Bridge Extraction Log

## Timestamp: 2025-09-24T10:30:00

## What Was Extracted
- Source: src/cost_optimizer.py (1,234 lines)
- Target: Outputs/llm-cost-analyzer (456 lines)
- Reduction: 63% (removed internal complexity)

## Value Created
- Standalone cost analysis tool
- No dependencies on agent infrastructure
- Pip-installable package

## Lessons Learned
- Pricing engine better as separate module
- Public API should be much simpler
- Examples more important than documentation
```

## Command Interface

### Basic Extraction
```bash
aget extract --from src/module.py --to Outputs/tool-name
```

### Advanced Options
```bash
aget extract \
    --from src/module.py \
    --to Outputs/tool-name \
    --type tool \
    --package \              # Create pip package
    --publish \              # Publish to PyPI
    --test \                 # Run validation tests
    --evolution "Extracted cost optimizer" \
    --version 1.0.0
```

### Interactive Mode
```bash
aget extract --interactive

🌉 Bridge Extraction Wizard
1. Select source (outputs/, src/, data/)
2. Choose extraction type (tool/pattern/library/docs)
3. Review transformations
4. Validate output
5. Document evolution
```

## Consequences

### Positive
- **Consistent quality**: All extractions follow same standards
- **Fast extraction**: Minutes instead of hours
- **Safe by default**: Automatic sensitive data removal
- **Traceable**: Evolution tracking built-in
- **Community ready**: Generated packages work immediately

### Negative
- **Over-sanitization**: Might remove too much
- **Simplification loss**: May lose valuable complexity
- **Maintenance**: Rules need updating

### Mitigations
- Allow rule overrides via config
- Preview mode before extraction
- Rollback capability

## Implementation Priority

HIGH - Critical for Gate 3 and enabling the framework vision of private→public value flow.

## References

- llm-manager-aget bridge.py implementation
- BRIDGE_EXTRACTION_PROCESS.md
- Security best practices for code sharing

---

*This ADR formalizes the bridge mechanism that transforms private exploration into public value.*