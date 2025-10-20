# Spec Engineer AGET - Usage Guide

## Purpose
Reverse engineer existing AGET agents into formal EARS specifications by analyzing session history and evolution documents.

## Quick Start (Any Machine)

### 1. Clone Template
```bash
gh repo clone aget-framework/template-spec-engineer-aget ~/spec-engineer
cd ~/spec-engineer
```

### 2. Wake Up
```bash
# Start new session
wake up
```

### 3. Request Extraction
```
User: "Reverse engineer ~/github/my-domain-vp-ai-aget"

Agent will:
1. Assess readiness using rubric (0-18 score)
2. Report score and recommendation
3. If score ≥6, ask for GO/NOGO confirmation
4. Extract patterns from sessions and evolution
5. Generate EARS specification
6. Save to target/.aget/specs/[agent_name]_REVERSE_ENGINEERED_v1.0.yaml
7. Report quality metrics
```

### 4. Review Output
```bash
# Check generated spec
cat ~/github/my-domain-vp-ai-aget/.aget/specs/*REVERSE_ENGINEERED*.yaml

# Review quality report (in agent session output)
```

## Proven Methodology

**Advanced Precedent** (Oct 2025):
- **Source**: 6,800 lines of sessions/evolution
- **Output**: 30-capability EARS specification
- **Result**: 1,109 lines validated production spec
- **Portfolio**: DOMAIN (any machine validated)

This precedent validates:
- ✅ Extraction quality achievable
- ✅ Cross-platform compatibility proven
- ✅ Timeline realistic (2-5 minutes per agent)

## Usage Patterns

### Pattern 1: Basic Extraction
```
User: "Reverse engineer ~/github/my-agent-aget"

Agent:
1. Assesses readiness (rubric scoring)
2. Reports: "14/18 - Moderately Reverse-Engineerable"
3. Asks: "Proceed with extraction? (GO/NOGO)"
User: "GO"
4. Extracts patterns, generates spec
5. Outputs: my_agent_aget_REVERSE_ENGINEERED_v1.0.yaml
6. Reports quality: 73% (completeness: 80%, accuracy: 65%, clarity: 70%)
```

### Pattern 2: Low Score Rejection
```
User: "Reverse engineer ~/github/experimental-aget"

Agent:
1. Assesses readiness
2. Reports: "4/18 - Not Reverse-Engineerable"
3. Explains: "Insufficient session history (0/3), no evolution docs (0/3)"
4. Recommends: "Build more with AGET first, then retry in 2 weeks"
5. STOPS (does not extract)
```

### Pattern 3: Comparison with Original
```
User: "Reverse engineer ~/github/my-agent-aget and compare with original spec"

Agent:
1. Performs extraction (as Pattern 1)
2. Detects original spec exists
3. Runs comparison tool
4. Reports:
   - Completeness: 85% (17/20 original capabilities captured)
   - New capabilities found: 3 (not in original)
   - Accuracy: 78% (EARS patterns match)
   - Recommendation: "Merge new capabilities into original spec v2.0"
```

## Requirements

### System Requirements
- Python 3.9+
- Git
- Access to target AGET agent directory
- Standard library only (no external dependencies)

### Target Agent Requirements
For best results, target agent should have:
- **Session files**: 10+ files in sessions/
- **Evolution files**: 5+ files in .aget/evolution/
- **Clear patterns**: Identifiable features/capabilities
- **Decision documentation**: Rationale in evolution files

**Minimum rubric score**: 6/18 (agent will refuse extraction below this)

## Troubleshooting

### Error: "Score too low (X/18) - not extractable"
**Cause**: Target agent lacks sufficient documentation

**Solution**:
1. Build more with target agent (add 5-10 sessions)
2. Document decisions in .aget/evolution/ (add 3-5 learning files)
3. Retry extraction in 1-2 weeks

### Error: "No sessions directory found"
**Cause**: Agent doesn't follow standard AGET structure

**Solution**:
1. Check if sessions in alternate location (docs/sessions/)
2. Manually specify: "Extract from ~/agent, sessions in docs/sessions/"
3. Agent will adjust paths accordingly

### Error: "Quality score below 60%"
**Cause**: Extraction accuracy low (ambiguous patterns, unclear sessions)

**Solution**:
1. Review quality report for specific issues
2. Agent will flag low-confidence capabilities
3. Manually review flagged capabilities before using spec
4. Consider improving source documentation and re-extracting

### Warning: "Capability temporal pattern uncertain"
**Cause**: Can't determine if ubiquitous/event-driven/state-driven

**Solution**:
1. Agent defaults to 'optional' pattern (safest)
2. Review flagged capabilities in output spec
3. Manually update temporal pattern based on domain knowledge

## Expected Timeline

- **Readiness assessment**: 30 seconds - 1 minute
- **Pattern extraction**: 1-3 minutes (depends on session count)
- **EARS generation**: 30 seconds
- **Quality validation**: 30 seconds
- **Total**: 2-5 minutes per agent

## Output Format

Generated specs follow EARS format v1.1:

```yaml
spec:
  id: SPEC-AGENT-NAME
  version: 1.0.0
  maturity: bootstrapping  # Conservative starting point
  format_version: '1.1'
  description: "[agent-name] capabilities (reverse engineered)"
  system_name: agent-name

capabilities:
  CAP-001:
    domain: session_management
    statement: "WHEN user says 'wake up', the SYSTEM shall read configuration and report readiness"
    pattern: event-driven
    trigger: user_command
    inputs: ["user command: 'wake up'"]
    outputs: ["agent identity", "git status", "readiness confirmation"]

  CAP-002:
    domain: feature_domain
    statement: "The SYSTEM shall [capability description]"
    pattern: ubiquitous
    inputs: [...]
    outputs: [...]

metadata:
  created: '2025-10-19'
  extraction_method: 'reverse_engineering'
  source_agent_path: '/path/to/agent'
  rubric_score: 14
  quality_confidence: 73.0
```

## Quality Metrics

**Completeness**: Percentage of observable features captured (target: ≥75%)

**Accuracy**: Correctness of EARS temporal patterns (target: ≥70%)

**Clarity**: Ambiguity detector warnings (target: ≥65% unambiguous)

**Overall Quality**: Weighted average (target: ≥70%)

## Best Practices

1. **Extract from well-documented agents first**: Start with agents scoring 15+ on rubric
2. **Review quality report**: Don't blindly trust generated spec
3. **Validate capabilities**: Spot-check 5-10 random capabilities for correctness
4. **Iterate**: If quality <70%, improve source documentation and re-extract
5. **Compare with original**: If original spec exists, use compare tool
6. **Cross-platform usage**: Test extraction on small agent first (verify compatibility)

## Reference Specs for Study

**Advanced Example**:
- Path: `products/presentations/ai-coe-2025-10-08/v4.0-law-insider-reverse-reengineered/TALE_SPEC_v4.0.yaml`
- Quality: Production-grade (30 capabilities, validated)
- Source: 6,800 lines of sessions/evolution
- Use case: Excellent example of successful reverse engineering

**Coordinator Example**:
- Path: `.aget/specs/COORDINATOR_SPEC_v3.0.yaml`
- Quality: Exemplary (35 capabilities, comprehensive)
- Maturity: Standard (test references, validation)
- Use case: Good reference for EARS patterns and structure

## Support

For issues or questions:
1. Check this guide's Troubleshooting section
2. Review extraction methodology: `docs/EXTRACTION_METHODOLOGY.md`
3. Understand consultant persona: `docs/PERSONA_GUIDE.md`
4. File issue: [aget-framework/template-spec-engineer-aget/issues]

---
*Enabling reverse engineering of AGET agents into professional specifications*
