# Reverse Specification Engineering - Extraction Methodology

## Core Philosophy

**Build first, document later - but with professional rigor**

Traditional software engineering:
```
Requirements → Design → Build → Test
```

Reverse specification engineering:
```
Code/Conversation → Working System → Extract Spec → Validate
```

**Applies to**:
- Python functions (20-100 lines) - **validation layer**
- Python scripts (100-500 lines) - **primary focus**
- Python modules (500-2000 lines) - **scaling**
- Full applications (multi-file, 2000+ lines) - **advanced**

## Recommended Progression

**Start small, validate methodology, scale up:**

### Level 1: Python Functions (Validation)
- **Size**: 20-100 lines
- **Complexity**: Single function, clear behavior
- **Quality expectation**: 85-95% (small surface area)
- **Purpose**: Prove methodology works

**Example**: Tax calculator function (50 lines) → 3-5 capability spec

### Level 2: Python Scripts (Primary Focus)
- **Size**: 100-500 lines
- **Complexity**: Multi-function, observable behavior
- **Quality expectation**: 75-85% (tractable complexity)
- **Purpose**: Real-world utility, provable extraction

**Example**: GitHub integration script (350 lines) → 8-12 capability spec

### Level 3: Applications (Advanced)
- **Size**: 2000+ lines (multi-file)
- **Complexity**: Cross-file dependencies, many capabilities
- **Quality expectation**: 60-70% (ambitious)
- **Purpose**: Demonstrate feasibility at scale

**Example**: Full AGET agent (6,800 lines) → 30 capability spec (Advanced precedent)

## Extraction Philosophy: Coding Agent Scaffolding

**NOT fully automated** - Tools provide framework for coding agent conversational analysis.

### Coding Agent Workflow

**Tools handle**:
- Rubric scoring (quantitative assessment)
- YAML formatting (structure generation)
- Quality validation (metrics calculation)
- File I/O (reading sessions, writing specs)

**Coding agent handles**:
- Pattern recognition (semantic understanding of conversations)
- Temporal classification (determining event-driven vs ubiquitous)
- Capability extraction (identifying what agent does from sessions)
- Context understanding (interpreting evolution decisions)

**This is collaborative intelligence**: Tool structure + agent semantics = quality extraction.

## Five-Phase Extraction Algorithm

### Phase 1: Readiness Assessment

**Purpose**: Determine if codebase has sufficient documentation/history for extraction

**Method**: Apply rubric scoring (6 categories, 0-3 each)

**Categories**:
1. **Development History** (25% weight)
   - Git commit history with clear messages
   - Session files (if AGET environment)
   - Code comments documenting decisions
   - Change logs, release notes

2. **Code Observability** (20% weight)
   - Clear function signatures and docstrings
   - Usage examples (tests, README)
   - Input/output patterns visible
   - Error cases documented

3. **Decision Documentation** (20% weight)
   - Design decisions documented (comments, docs, evolution files)
   - Rationale for choices clear
   - Trade-offs documented
   - Alternative approaches noted

4. **Pattern Clarity** (15% weight)
   - Reusable components identified
   - Design patterns visible
   - Consistent code structure
   - Pattern usage clear

5. **Constraint Discovery** (10% weight)
   - Boundary conditions tested
   - Error cases documented
   - Validation logic clear
   - Constraints explicit

6. **Quality Attributes** (10% weight)
   - Performance characteristics measurable
   - Reliability indicators present
   - Security considerations noted
   - Scalability considerations documented

**Scoring**:
- **15-18** (83-100%): Highly Reverse-Engineerable → Proceed
- **11-14** (61-82%): Moderately Reverse-Engineerable → Proceed with caveats
- **6-10** (33-60%): Poorly Reverse-Engineerable → Significant effort required
- **0-5** (0-32%): Not Reverse-Engineerable → **STOP** (build more first)

**Output**: Rubric score + category breakdown + recommendation

### Phase 2: Pattern Extraction

**Purpose**: Mine code, development history, and documentation for behavioral patterns

**Method**: Coding agent semantic analysis with tool scaffolding

**Sources** (priority order):
1. **Code structure** - Functions, classes, modules (primary)
2. **Tests** - What behaviors are validated (high confidence)
3. **Development history** - Git commits, session files (if AGET)
4. **Documentation** - Comments, docstrings, evolution files

**Code Analysis**:
```python
def extract_from_code(source_files):
    """
    Coding agent reads Python code, identifies:
    - Function signatures (inputs → outputs)
    - Class methods (object capabilities)
    - Control flow (conditional, looping patterns)
    - Error handling (exception patterns)
    - External dependencies (API calls, file I/O)
    """
    patterns = []

    for source_file in source_files:
        # Coding agent analyzes code semantically
        # (Understands intent, not just syntax)

        # Example extraction:
        # def validate_input(data):
        #     if not data: raise ValueError()
        # → Pattern: Always validates input (ubiquitous)

        functions = extract_function_signatures(source_file)
        control_flow = analyze_control_flow(source_file)

        patterns.extend(infer_capabilities(functions, control_flow))

    return deduplicate_patterns(patterns)
```

**Development History Analysis** (if available):
```python
def extract_from_history(session_files, evolution_files, commits):
    """
    Coding agent reads development artifacts, identifies:
    - Design decisions (why this approach chosen)
    - Constraints discovered (what limitations found)
    - Usage patterns (from sessions/commits)
    - Quality evolution (performance improvements)
    """
    patterns = []
    quality_attributes = []

    for learning_file in evolution_files:
        # Coding agent analyzes "Problem" and "Learning" sections

        # Example:
        # Problem: "Migration took 45 minutes (too slow)"
        # Learning: "Parallel processing reduces to 15 minutes"
        # → Quality attribute: Performance requirement <30min

        problems = extract_problem_section(learning_file)
        learnings = extract_learning_section(learning_file)

        constraints.extend(infer_constraints(problems, learnings))
        quality_attributes.extend(infer_quality_reqs(learnings))

    return constraints, quality_attributes
```

**Pattern Structure**:
```python
class Pattern:
    domain: str           # Capability category (session_management, data_processing)
    action: str          # What system does ("read configuration", "process data")
    trigger: Optional[str]   # Event that starts action ("user says 'wake up'")
    state: Optional[str]     # State during action ("while session active")
    condition: Optional[str] # Condition for action ("if data valid")
    precondition: Optional[str] # Optional requirement ("where cache available")
    frequency: str       # How often ("always", "sometimes", "rarely")
    inputs: List[str]    # What goes in
    outputs: List[str]   # What comes out
    confidence: float    # How certain (0.0-1.0)
```

**Output**: List of extracted patterns with confidence scores

### Phase 3: EARS Statement Generation

**Purpose**: Convert patterns into formal EARS temporal pattern statements

**Method**: Classify patterns → Generate statements

**Temporal Pattern Classification**:

**1. Ubiquitous** (pattern.frequency == 'always')
```
Pattern: Agent always validates input before processing
→ "The SYSTEM shall validate input before processing"
```

**2. Event-Driven** (pattern.trigger exists)
```
Pattern: When user says 'wake up', agent reads configuration
→ "WHEN user says 'wake up', the SYSTEM shall read configuration and report readiness"
```

**3. State-Driven** (pattern.state exists)
```
Pattern: While session active, agent maintains evolution history
→ "WHILE session is active, the SYSTEM shall maintain evolution history in .aget/evolution/"
```

**4. Conditional** (pattern.condition exists)
```
Pattern: If score below threshold, reject extraction
→ "IF rubric score < 6 THEN the SYSTEM shall reject extraction and recommend building more documentation"
```

**5. Optional** (pattern.precondition exists OR uncertainty)
```
Pattern: Where ambiguity detector available, run clarity check
→ "WHERE ambiguity detector is available, the SYSTEM shall validate spec clarity and report warnings"

Pattern: Unclear temporal classification (low confidence)
→ "WHERE [inferred precondition], the SYSTEM shall [action]"  # Conservative default
```

**Classification Logic**:
```python
def classify_temporal_pattern(pattern):
    """
    Coding agent determines temporal pattern based on:
    - Frequency analysis (always → ubiquitous)
    - Trigger identification (event mention → event-driven)
    - State detection (continuous activity → state-driven)
    - Condition presence (if/then → conditional)
    - Default: optional (when uncertain)
    """
    if pattern.frequency == 'always' and not pattern.trigger:
        return 'ubiquitous'
    elif pattern.trigger:
        return 'event-driven'
    elif pattern.state:
        return 'state-driven'
    elif pattern.condition:
        return 'conditional'
    else:
        return 'optional'  # Conservative default
```

**Confidence Handling**:
- High confidence (≥0.8): Use determined pattern
- Medium confidence (0.5-0.8): Use pattern, flag for review
- Low confidence (<0.5): Default to 'optional', flag for review

**Output**: List of EARS-formatted capability statements with confidence flags

### Phase 4: Spec Assembly

**Purpose**: Structure capabilities into YAML specification format

**Method**: Apply SPEC_FORMAT_v1.1 structure

**Spec Structure**:
```yaml
spec:
  id: SPEC-AGENT-NAME-UPPERCASE
  version: 1.0.0
  maturity: bootstrapping  # Start conservative
  format_version: '1.1'
  description: "[agent-name] capabilities (reverse engineered)"
  system_name: agent-name

capabilities:
  CAP-001:
    domain: [inferred_domain]
    statement: "[EARS formatted statement]"
    pattern: [ubiquitous|event-driven|state-driven|conditional|optional]
    trigger: [if event-driven]
    state: [if state-driven]
    condition: [if conditional]
    precondition: [if optional]
    inputs: [extracted inputs]
    outputs: [extracted outputs]
    confidence: [0.0-1.0, flagged if <0.8]

metadata:
  created: [date]
  extraction_method: 'reverse_engineering'
  source_agent_path: [path]
  rubric_score: [0-18]
  quality_confidence: [0-100%]
  law_insider_precedent: true  # Reference proven methodology
  notes: |
    Extracted via coding agent semantic analysis.
    Low-confidence capabilities (<0.8) flagged for manual review.
```

**Maturity Level**: Start with 'bootstrapping' (conservative)
- Can be upgraded to 'minimal' after manual review
- Then 'standard' after validation
- Finally 'exemplary' after production usage

**Output**: YAML specification structure

### Phase 5: Quality Scoring

**Purpose**: Validate extraction quality against benchmarks

**Method**: Calculate three quality dimensions

**1. Completeness** (target: ≥75%)
```python
def calculate_completeness(spec, source_agent_path):
    """
    Measure: % of observable features captured in spec

    Method:
    1. Identify observable features:
       - Tools in .aget/tools/ → Capabilities
       - Patterns in patterns/ → Capabilities
       - Commands in scripts/ → Capabilities
       - Sessions usage → Capabilities

    2. Count capabilities in extracted spec

    3. Completeness = (extracted / observable) * 100
    """
    observable = count_observable_features(source_agent_path)
    extracted = len(spec['capabilities'])

    return (extracted / observable) * 100 if observable > 0 else 0
```

**2. Accuracy** (target: ≥70%)
```python
def calculate_accuracy(spec):
    """
    Measure: % of EARS statements with correct temporal patterns

    Method:
    1. Validate EARS syntax (WHEN/WHILE/IF/WHERE present)
    2. Check pattern consistency (event-driven has trigger, etc.)
    3. Verify inputs/outputs make sense
    4. Confirm domain categorization reasonable

    Accuracy = (valid_statements / total_statements) * 100
    """
    valid_count = 0
    total_count = len(spec['capabilities'])

    for cap in spec['capabilities'].values():
        if validate_ears_syntax(cap) and validate_pattern_consistency(cap):
            valid_count += 1

    return (valid_count / total_count) * 100 if total_count > 0 else 0
```

**3. Clarity** (target: ≥65%)
```python
def calculate_clarity(spec):
    """
    Measure: % of statements with low ambiguity

    Method:
    1. Run ambiguity_detector.py on each statement
    2. Count warnings (vague terms, unclear scope, missing context)
    3. Clarity = (statements_without_warnings / total) * 100
    """
    clear_count = 0
    total_count = len(spec['capabilities'])

    for cap in spec['capabilities'].values():
        warnings = run_ambiguity_detector(cap['statement'])
        if len(warnings) == 0:
            clear_count += 1

    return (clear_count / total_count) * 100 if total_count > 0 else 0
```

**Overall Quality**:
```
Quality = (Completeness * 0.5) + (Accuracy * 0.3) + (Clarity * 0.2)
```

**Weighting rationale**:
- Completeness (50%): Most important (missing capabilities = incomplete spec)
- Accuracy (30%): Critical (wrong patterns = misleading spec)
- Clarity (20%): Important (ambiguous = hard to implement from)

**Benchmark**: Advanced achieved 70%+ overall quality → This is the standard

**Output**: Quality report with three dimensions + overall score

## Edge Cases & Mitigation

### Edge Case 1: No Sessions Directory
**Problem**: Agent doesn't follow standard structure

**Mitigation**:
```python
# Check alternate locations
paths_to_check = [
    'sessions/',
    'docs/sessions/',
    'workspace/sessions/',
    '.aget/sessions/'
]

for path in paths_to_check:
    if exists(agent_path / path):
        session_dir = path
        break
else:
    # Ask user
    print("No sessions directory found. Where are sessions stored?")
```

### Edge Case 2: Evolution Files in Alternate Format
**Problem**: Not using L## naming convention

**Mitigation**:
```python
# Try multiple patterns
evolution_patterns = [
    'L*.md',  # Standard
    'DEC-*.md',  # Decision docs
    'DISC-*.md',  # Discovery docs
    '*.md'  # Fallback (all markdown)
]
```

### Edge Case 3: Very Low Quality (<60%)
**Problem**: Extraction produces low-confidence spec

**Mitigation**:
```
1. Report quality score with breakdown
2. Identify root cause:
   - Low completeness → "Only 5 sessions (need 10+)"
   - Low accuracy → "Unclear temporal patterns (ambiguous sessions)"
   - Low clarity → "Vague action descriptions (no input/output examples)"
3. Recommend improvement:
   - "Add 5 more diverse sessions"
   - "Document decisions in evolution/"
   - "Add usage examples to sessions"
4. Offer partial extraction:
   - "Extract high-confidence capabilities only (12/20)"
   - "Flag low-confidence for manual review"
```

### Edge Case 4: Temporal Pattern Uncertainty
**Problem**: Can't determine if ubiquitous vs event-driven

**Mitigation**:
```python
# Conservative default + flag
capability = {
    'pattern': 'optional',  # Safest assumption
    'confidence': 0.4,  # Low confidence
    'note': 'Temporal pattern uncertain - manual review recommended',
    'alternatives': ['event-driven', 'ubiquitous'],  # Possible patterns
    'rationale': 'Insufficient trigger evidence in sessions'
}
```

## Validation Strategy

### Internal Validation (Automatic)
1. YAML syntax validation (parseable)
2. EARS pattern syntax (WHEN/WHILE/IF/WHERE present)
3. Pattern consistency (event-driven has trigger field)
4. Quality scoring (completeness, accuracy, clarity)

### External Validation (Manual)
1. Spot-check 5-10 capabilities (do they match actual code behavior?)
2. Review low-confidence flags (<0.8)
3. Compare with original spec (if exists)
4. Run extracted spec through ambiguity detector
5. Test a few capabilities (do they exist in the codebase?)

### Quality Benchmarks by Complexity

**Quality expectations vary by codebase size:**

**Python Functions** (20-100 lines):
- Expected: 85-95% quality
- Capabilities: 2-5
- Validation: Easy spot-check

**Python Scripts** (100-500 lines):
- Expected: 75-85% quality
- Capabilities: 5-15
- Validation: Test against code behavior

**Python Modules** (500-2000 lines):
- Expected: 65-75% quality
- Capabilities: 15-30
- Validation: Compare with tests/docs

**Full Applications** (2000+ lines):
- Expected: 60-70% quality
- Capabilities: 30-50+
- Example: Advanced (6,800 lines → 30 caps → 70%+ quality)

## Success Criteria

**Extraction succeeds if**:
1. ✅ Rubric score ≥ 6/18 (codebase documented enough)
2. ✅ YAML output valid (parseable)
3. ✅ EARS patterns correctly applied (syntax valid)
4. ✅ Quality meets complexity benchmark (75-85% for scripts, 60-70% for applications)
5. ✅ Capabilities count reasonable for codebase size
6. ✅ Low-confidence capabilities flagged (<0.8)
7. ✅ Manual spot-check validates correctness (5/5 capabilities accurate)

**Extraction fails if**:
1. ❌ Rubric score < 6/18 (insufficient documentation/history)
2. ❌ Quality < 60% (too many errors/gaps)
3. ❌ No patterns extracted (empty capabilities section)
4. ❌ All capabilities low-confidence (<0.5)

## Continuous Improvement

### Learning from Extractions

Track extraction results to improve methodology:

```yaml
extraction_history:
  - target: github_integration.py (Python script)
    rubric_score: 13/18
    quality: 78%
    capabilities: 8
    lessons:
      - "Clear function signatures enabled high accuracy"
      - "Tests provided excellent usage examples"
      - "Quality within script benchmark (75-85%)"

  - target: data_processor.py (Python module)
    rubric_score: 10/18
    quality: 68%
    capabilities: 18
    lessons:
      - "Limited docstrings reduced clarity score"
      - "Code structure clear, but missing design docs"
      - "Quality acceptable for module complexity (65-75%)"

  - target: Advanced AGET (Full application)
    rubric_score: 16/18
    quality: 70%+
    capabilities: 30
    lessons:
      - "Extensive session/evolution history (6,800 lines)"
      - "Advanced use case - demonstrates feasibility at scale"
      - "Quality at upper end of application benchmark (60-70%)"
```

### Pattern Recognition Improvement

As more codebases extracted, refine heuristics:
- Which code patterns → which capabilities?
- Which test patterns → which behaviors?
- Which documentation types most predictive of success?

---

*Extract → Maintain → Evolve formal specifications for Python code through semantic understanding*
