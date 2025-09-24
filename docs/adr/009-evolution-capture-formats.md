# ADR-009: Evolution Capture Formats

**Date**: 2025-09-24
**Status**: Proposed
**Context**: Standardize evolution tracking based on llm-manager-aget experience

## Decision

Establish standard formats and templates for capturing agent evolution, learning, and decision-making in `.aget/evolution/`.

## Context

The evolution tracking in llm-manager-aget proved invaluable for understanding decisions and preserving learning. However, the free-form approach led to inconsistency. We need standardized formats that are:
1. Machine-readable for analysis
2. Human-readable for understanding
3. Consistent across agents
4. Searchable and indexable

## Evolution Entry Types

### 1. Decision Records

**File**: `.aget/evolution/decision_YYYYMMDD_HHMMSS.md`

```markdown
# Decision: [Brief Title]

## Date: 2025-09-24T10:30:00

## Context
What situation required a decision?

## Options Considered
1. **Option A**: Description
   - Pros: ...
   - Cons: ...

2. **Option B**: Description
   - Pros: ...
   - Cons: ...

## Decision Made
**Chosen**: Option A

## Rationale
Why this option was selected.

## Consequences
- Immediate: What changes now
- Future: What this enables/prevents

## Metadata
- Category: architecture|optimization|feature|refactor
- Impact: high|medium|low
- Reversible: yes|no|partial

---
*Captured by: agent|human*
```

### 2. Discovery Records

**File**: `.aget/evolution/discovery_YYYYMMDD_HHMMSS.md`

```markdown
# Discovery: [Pattern/Insight Name]

## Date: 2025-09-24T10:30:00

## What Was Discovered
Brief description of the pattern or insight.

## How It Was Found
- Context: What led to this discovery
- Method: How it was identified
- Validation: How it was verified

## Evidence
```python
# Code example or data supporting the discovery
```

## Applications
- Where this can be applied
- Expected benefits
- Potential risks

## Value Assessment
- Savings: $X or Y%
- Efficiency: Time/resource improvement
- Quality: How it improves outcomes

## Next Steps
- [ ] Test in production
- [ ] Document in patterns
- [ ] Extract to public Output

## Metadata
- Type: pattern|optimization|bug|insight
- Confidence: high|medium|low
- Reusability: universal|specific|limited

---
*Discovered during: [activity/exploration]*
```

### 3. Extraction Records

**File**: `.aget/evolution/extraction_YYYYMMDD_HHMMSS.md`

```markdown
# Extraction: [Tool/Pattern Name]

## Date: 2025-09-24T10:30:00

## Source
- Location: outputs/analysis/module.py
- Type: tool|pattern|library|documentation
- Size: X lines/files

## Target
- Location: Outputs/tool-name
- Format: standalone|package|pattern
- Version: 1.0.0

## Transformation Process
1. **Removed**: API keys, internal URLs
2. **Simplified**: Complex internal APIs
3. **Added**: Documentation, examples
4. **Validated**: Import test, basic functionality

## Value Created
- What problem it solves
- Who can benefit
- How it improves on existing solutions

## Metrics
- Code reduction: X% (internal vs public)
- Dependencies: Before: X, After: Y
- Complexity: Cyclomatic complexity reduced by Z

## Distribution
- [ ] Published to PyPI
- [ ] Shared on GitHub
- [ ] Documented in README

## Metadata
- Bridge-type: full|partial|pattern
- Standalone: yes|no
- License: MIT|Apache|GPL

---
*Extracted via: manual|automated|assisted*
```

### 4. Learning Records

**File**: `.aget/evolution/learning_YYYYMMDD_HHMMSS.md`

```markdown
# Learning: [Lesson Title]

## Date: 2025-09-24T10:30:00

## Lesson Learned
What was learned and why it matters.

## Context
- What happened: The situation
- What was expected: Initial assumption
- What actually occurred: Reality

## Root Cause
Why did this happen?

## Prevention/Application
- How to avoid this issue
- How to apply this learning

## Impact on Future Work
- Changes to make
- Patterns to follow/avoid
- Tools to build/modify

## Related Items
- Decisions: [decision_20250924_103000.md]
- Discoveries: [discovery_20250924_110000.md]
- Issues: #123, #456

## Metadata
- Type: mistake|success|optimization|insight
- Severity: critical|important|minor
- Applicability: universal|project|situational

---
*Learned from: [experience/experiment/failure]*
```

### 5. Experiment Records

**File**: `.aget/evolution/experiment_YYYYMMDD_HHMMSS.md`

```markdown
# Experiment: [Hypothesis/Test Name]

## Date: 2025-09-24T10:30:00

## Hypothesis
What we're testing and why.

## Method
1. Setup: Initial conditions
2. Test: What was changed/tried
3. Measurement: How success is determined

## Results
- Expected: What we thought would happen
- Actual: What happened
- Data: Supporting metrics/evidence

## Analysis
Why did we get these results?

## Conclusions
- Hypothesis: confirmed|rejected|partial
- Learnings: Key takeaways
- Applications: Where to apply results

## Next Experiments
- What to test next based on results
- New hypotheses formed

## Metadata
- Status: complete|ongoing|abandoned
- Success: yes|no|partial
- Reproducible: yes|no|conditional

---
*Experiment type: performance|feature|optimization*
```

## Command Interface

### Creating Evolution Entries

```bash
# Interactive mode
aget evolution

Select type:
1. Decision
2. Discovery
3. Extraction
4. Learning
5. Experiment

# Direct creation
aget evolution --type decision "Choose GPT-4 over Claude"
aget evolution --type discovery "Found 70% cost savings pattern"
aget evolution --type extraction "Extracted cost analyzer tool"
aget evolution --type learning "API keys must be removed before extraction"
aget evolution --type experiment "Test caching for repeated queries"
```

### Viewing Evolution

```bash
# List recent evolution
aget evolution --list

Recent Evolution:
- 2025-09-24 10:30 [Decision] Choose TypeScript over Python
- 2025-09-24 11:00 [Discovery] Caching reduces costs 40%
- 2025-09-24 11:30 [Extraction] Cost analyzer tool

# View specific entry
aget evolution --view decision_20250924_103000

# Search evolution
aget evolution --search "cost optimization"

# Generate summary
aget evolution --summary --days 30
```

### Evolution Analysis

```bash
# Analyze patterns
aget evolution --analyze

Evolution Analysis (Last 30 days):
- Decisions: 15 (60% architecture, 40% optimization)
- Discoveries: 8 (5 extracted to Outputs)
- Learnings: 12 (3 critical, 9 important)
- Experiments: 6 (4 successful, 2 failed)

Top Patterns:
1. Cost optimization through model selection
2. Caching for repeated queries
3. Interface simplification for public tools
```

## File Naming Convention

```
{type}_{YYYYMMDD}_{HHMMSS}[_brief_description].md

Examples:
- decision_20250924_103000_chose_typescript.md
- discovery_20250924_110000_cost_pattern.md
- extraction_20250924_113000_llm_analyzer.md
- learning_20250924_120000_api_security.md
- experiment_20250924_130000_cache_test.md
```

## Metadata Schema

Each entry includes structured metadata for querying:

```yaml
metadata:
  type: decision|discovery|extraction|learning|experiment
  date: 2025-09-24T10:30:00
  category: architecture|optimization|feature|security
  impact: high|medium|low
  tags: [cost, optimization, llm, api]
  related: [file1.md, file2.md]
  author: agent|human|system
```

## Integration with Git

Evolution entries should be:
1. **Committed immediately** after creation
2. **Tagged** for major milestones
3. **Never modified** (append-only)
4. **Included in releases** for context

## Consequences

### Positive
- **Preserves context**: Decisions and learnings never lost
- **Enables analysis**: Can identify patterns over time
- **Supports learning**: New team members understand history
- **Improves quality**: Learn from past mistakes

### Negative
- **Overhead**: Takes time to document
- **Storage**: Can accumulate many files
- **Discipline**: Requires consistent use

### Mitigations
- Templates reduce documentation time
- Archive old entries after 1 year
- Automated reminders for documentation

## Implementation Priority

HIGH - Evolution tracking is core to the AGET framework's learning capability and was proven valuable in llm-manager-aget.

## References

- llm-manager-aget evolution tracking
- ADR format (architecture decision records)
- Scientific lab notebook practices

---

*This ADR ensures that agent learning and evolution are captured consistently and usefully.*