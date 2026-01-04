# Template: Specification Engineer

> **Reverse engineer Python code into formal EARS specifications**

**Extract → Maintain → Evolve** specifications for any Python codebase

**Current Version**: v3.1.0
**Persona**: Consultant (solutions focus, professional analysis)
**Contract Tests**: 158 (100% passing)

---

## Purpose

Create formal EARS specifications from existing Python code through conversational extraction:
- **Analyze** development history (sessions, commits, comments)
- **Understand** code behavior (functions, inputs, outputs)
- **Extract** capabilities (what system must do)
- **Generate** unambiguous specifications (aerospace-grade requirements)

**Methodology**: Coding agent semantic understanding (not automated parsing)

**Primary Focus**: Python scripts and tools (100-500 lines)

**Progression Path**: Functions → Scripts → Modules → Applications

**Dual Purpose**: Not just extraction, but ongoing specification maintenance and evolution

---

## Use Cases

### 1. AGET Agent Tooling (Primary Development Context)
**Specify tools and agents in AGET ecosystem**:
- `.aget/tools/*.py` scripts (monitoring, GitHub integration, etc.)
- `.aget/patterns/*.py` automation patterns
- Full AGET agents (after validating on scripts)

**Example**: Specify private-github-AGET's tools → formal EARS specifications

### 2. General Python Projects
**Point template at any Python codebase**:
- Utility scripts (data processing, automation)
- API clients (REST integrations, service wrappers)
- CLI tools (command-line utilities)
- Library functions (reusable components)

**Example**: Specify web scraping script → formal capability specification

### 3. Legacy Code Documentation
**Create specifications for undocumented code**:
- Read development history (commits, comments) or code structure
- Analyze code behavior and patterns
- Extract implicit requirements into formal spec
- Maintain spec as code evolves

**Example**: 500-line legacy script with no docs → 15-capability EARS spec

### 4. Specification Maintenance (Ongoing)
**Maintain specifications as primary artifacts**:
- Code changes → update specification
- Specification changes → guide code updates
- Version both together (code + spec in sync)

**Example**: Add new feature → update spec first → implement from spec

---

## Quick Start

### 1. Clone Template
```bash
gh repo clone aget-framework/template-spec-engineer-aget ~/spec-engineer
cd ~/spec-engineer
```

### 2. Extract Spec from Python Script

```
User: "Reverse engineer ~/my-project/github_integration.py"

Agent:
1. Assesses readiness (rubric scoring: 0-18)
2. Reports: "13/18 - Moderately Reverse-Engineerable"
3. Asks: "Proceed with extraction? (GO/NOGO)"

User: "GO"

Agent:
4. Reads code structure and development history
5. Understands script capabilities (issue creation, PR management, etc.)
6. Extracts 8 capabilities from analysis
7. Generates EARS specification
8. Saves to: my-project/specs/github_integration_SPEC_v1.0.yaml
9. Reports quality: "78% (completeness: 75%, accuracy: 85%, clarity: 75%)"
```

### 3. Review and Maintain Spec
```bash
# Review extracted specification
cat ~/my-project/specs/github_integration_SPEC_v1.0.yaml

# Update spec as code evolves (ongoing maintenance)
# Consultant persona provides guidance on spec quality and completeness
```

---

## Tools

### assess_agent.py - Readiness Assessment
```bash
python3 .aget/tools/assess_agent.py ~/my-project/github_integration.py \
  --development-history 2 \
  --code-observability 3 \
  --decision-documentation 2 \
  --pattern-clarity 2 \
  --constraint-discovery 1 \
  --quality-attributes 2

# Output: 12/18 - Moderately extractable
```

### extract_spec.py - Semantic Extraction Framework
```bash
# Check readiness only
python3 .aget/tools/extract_spec.py ~/my-project/github_integration.py --check-only

# Full extraction via coding agent (not automated)
# Use conversationally as shown in Quick Start
```

### spec_quality_scorer.py - Quality Validation
```bash
python3 .aget/tools/spec_quality_scorer.py \
  ~/my-project/specs/github_integration_SPEC_v1.0.yaml \
  ~/my-project

# Output:
# Completeness: 75.0%
# Accuracy: 85.0%
# Clarity: 75.0%
# Overall: 78.3% ✅ PRODUCTION-GRADE
```

### compare_specs.py - Specification Comparison
```bash
python3 .aget/tools/compare_specs.py \
  ~/my-project/specs/github_integration_SPEC_v1.0.yaml \
  ~/my-project/specs/github_integration_SPEC_v2.0.yaml

# Output:
# Coverage: 87% (7/8 capabilities matched)
# Missing: 1 capability
# New: 3 capabilities discovered
```

---

## Rubric Scoring

6-category readiness assessment (0-18 total):

1. **Development History** (25% weight)
   - Git commit history, session files (AGET), code comments documenting decisions
   - Change logs, release notes, development artifacts

2. **Code Observability** (20%)
   - Clear function signatures, docstrings present
   - Usage examples (tests, README), input/output patterns visible

3. **Decision Documentation** (20%)
   - Design decisions documented (comments, docs, evolution files)
   - Rationale for choices clear, trade-offs noted

4. **Pattern Clarity** (15%)
   - Reusable components identified, design patterns visible
   - Consistent code structure

5. **Constraint Discovery** (10%)
   - Boundary conditions tested, error cases documented
   - Validation logic clear

6. **Quality Attributes** (10%)
   - Performance characteristics measurable
   - Reliability indicators present, security considerations noted

**Thresholds**:
- **15-18**: Highly extractable (rich documentation/history, expect 75%+ quality)
- **11-14**: Moderately extractable (some gaps, expect 65-75%)
- **6-10**: Poorly extractable (significant inference needed, expect 50-65%)
- **0-5**: Not extractable (minimal documentation/history)

---

## Quality Benchmarks

Quality expectations by code complexity (progression path):

### Python Functions (20-100 lines) - Validation Layer
- **Expected capabilities**: 2-5
- **Completeness**: 80-95% (small surface area)
- **Accuracy**: 90-100% (clear behavior)
- **Overall**: 85-95% quality

### Python Scripts (100-500 lines) ← **PRIMARY FOCUS**
- **Expected capabilities**: 5-15
- **Completeness**: 70-85% (manageable complexity)
- **Accuracy**: 80-90% (observable behavior)
- **Overall**: 75-85% quality

### Python Modules (500-2000 lines) - Scaling
- **Expected capabilities**: 15-30
- **Completeness**: 60-75% (increasing complexity)
- **Accuracy**: 75-85% (some inference needed)
- **Overall**: 65-75% quality

### Full Applications (multi-file, 2000+ lines) - Advanced
- **Expected capabilities**: 30-50+
- **Completeness**: 50-70% (ambitious)
- **Accuracy**: 70-80% (complex behavior)
- **Overall**: 60-70% quality

**Advanced Precedent** (Advanced Use Case):
- **Input**: 6,800 lines (AGET agent with extensive session/evolution history)
- **Output**: 30 capabilities, 70%+ quality
- **Demonstrates**: Feasibility at application scale (validate at script level first)

---

## Getting Started: Recommended Progression

### Level 1: Validate Methodology (Python Functions)
**Start here**: Single-function scripts (20-100 lines)

**Why**: Prove template works at small scale
- Clear boundaries (one function = one spec)
- Easy to validate (does spec match function?)
- Build confidence in methodology

**Example**:
```python
# simple_calculator.py (50 lines)
def calculate_tax(amount, rate):
    # ... implementation
```
→ Generates 3-5 capability spec (addition, multiplication, rounding, validation, error handling)

### Level 2: Scale to Scripts (Primary Use Case)
**Next**: Multi-function scripts (100-500 lines)

**Why**: Tractable complexity, real-world utility
- Still single-file (manageable)
- Multiple capabilities (5-15 typical)
- Observable behavior (clear inputs/outputs)

**Example**: GitHub integration script → 8-12 capabilities across 3-4 domains

### Level 3: Modules and Applications (Advanced)
**Finally**: Multi-file systems (500+ lines)

**Why**: Requires multiple session analysis, complex behavior
- Cross-file dependencies
- Many capabilities (20-40+)
- Complex interactions

**Example**: Full AGET agent → 30 capabilities (validated precedent)

---

## Documentation

- **USAGE_GUIDE.md**: Quick start, troubleshooting, requirements
- **PERSONA_GUIDE.md**: Consultant rationale, implementation guidelines
- **EXTRACTION_METHODOLOGY.md**: 5-phase algorithm, validated precedent, validation

---

## Contract Tests

32 tests validate framework (100% passing):
- Identity protocol (7 tests)
- Scoped write permissions (5 tests)
- Rubric scoring logic (4 tests)
- Pattern extraction (6 tests)
- EARS generation (4 tests)
- Quality scoring (3 tests)
- End-to-end workflows (3 tests)

```bash
pytest tests/test_identity.py tests/test_scoped_writes.py \
  tests/test_rubric_scoring.py tests/test_pattern_extraction.py \
  tests/test_ears_generation.py tests/test_quality_scoring.py \
  tests/test_end_to_end.py -v

# Expected: 32 passed in 0.04s
```

---

## Requirements

- **System**: Python 3.9+, Git
- **Target Code**: Python codebase with development history (commits, comments, session files, or tests)
- **Minimum Documentation**: Rubric score ≥6 (basic observability required)
- **Dependencies**: None (standard library only, self-contained)

---

## Cross-Platform Ready

Designed for cross-machine use:

1. Clone: `gh repo clone aget-framework/template-spec-engineer-aget`
2. Point at any Python codebase (AGET agents, scripts, modules)
3. No hardcoded paths (semantic extraction)
4. Generate specs locally (no network dependencies)

---

## Specification

| Attribute | Value |
|-----------|-------|
| **Governed By** | [AGET_TEMPLATE_SPEC v3.1](https://github.com/aget-framework/aget/blob/main/specs/AGET_TEMPLATE_SPEC.md) |
| **Foundation** | [WORKER_TEMPLATE_SPEC v1.0](https://github.com/aget-framework/aget/blob/main/specs/WORKER_TEMPLATE_SPEC_v1.0.yaml) |
| **Archetype** | Spec_Engineer |
| **Manifest Version** | 3.0 |
| **Contract Tests** | 158 tests |

### Key Capabilities

| ID | Capability | Pattern |
|----|------------|---------|
| CAP-001 | Wake Protocol | event-driven |
| CAP-009 | Wind Down Protocol | event-driven |
| CAP-019 | Read-Only Mode | optional |
| CAP-SPEC | EARS Authoring | ubiquitous |

Validate compliance: `pytest tests/ -v`

See: [Full specification](https://github.com/aget-framework/aget/tree/main/specs)

---

## License

**AGET Framework (This Template)**: Apache License 2.0

This template and all framework code (`.aget/` structure, patterns, protocols) are licensed under the Apache License 2.0. This ensures:

- **Patent protection** for all adopters
- **Freedom to fork**, modify, and redistribute
- **Enterprise-safe** licensing for production use

See [LICENSE](LICENSE) for full terms.

**Your Agent Instance**: Your Choice

When you create an agent from this template, **you choose the license** for your specific instance:

- Keep it Apache 2.0 (recommended for public/shared agents)
- Make it private (all rights reserved)
- Choose MIT, GPL, or any other license

**The framework is open commons. What you build with it is yours.**

### Why Apache 2.0?

AGET is production infrastructure for agent configuration and lifecycle management. Apache 2.0 provides:

1. **Patent Grant**: Contributors can't patent their contributions and sue adopters
2. **Patent Retaliation**: If someone sues for patent infringement, they lose their license
3. **Ecosystem Immunity**: The standard stays free even as it becomes valuable
4. **Enterprise Adoption**: Legal teams approve Apache 2.0 more readily than other licenses

This follows the precedent of Kubernetes, Android, Swift, and other infrastructure projects.

### Upgrading Existing Agents

If you created an agent from an earlier MIT-licensed template, no action is required. Your agent remains valid under MIT (grandfathered).

To upgrade to Apache 2.0 for patent protection benefits, see the upgrade guide in the [AGET Framework documentation](https://github.com/aget-framework).

---

**Extract → Maintain → Evolve formal specifications for Python code through semantic understanding**
