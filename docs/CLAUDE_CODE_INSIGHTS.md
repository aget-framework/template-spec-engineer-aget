# Claude Code Engineering Insights for AGET

*Source: "How Claude Code is built" by Gergely Orosz, The Pragmatic Engineer (Sep 2025)*
*Created: 2025-09-24*

## Executive Summary

Analysis of Claude Code's architecture and development practices reveals key insights that validate AGET's approach and suggest future enhancements. The core philosophy of simplicity, minimal wrapper around AI models, and rapid iteration aligns perfectly with AGET's design principles.

## Key Architectural Principles

### 1. **Simplicity Above All**
> "With every design decision, we almost always pick the simplest possible option"

- No virtualization, runs locally
- Minimal business logic
- Delete code with each model improvement
- **AGET Alignment**: ✅ Perfect match with our philosophy

### 2. **90% Self-Written**
- Claude Code is 90% written by itself
- **AGET Opportunity**: Use AGET to build AGET more extensively
- Create self-improvement patterns

### 3. **"On Distribution" Tech Stack**
- Choose technologies the AI already knows well
- TypeScript/React chosen for Claude's strengths
- **AGET Implication**: Python is perfect (very "on distribution")

## Development Velocity Insights

### Metrics from Claude Code Team
- **5 PRs/day/engineer** (vs industry norm of 1-2)
- **60-100 internal releases/day**
- **1 external release/day**
- **20 prototypes in 2 days** for single feature

### AGET Velocity Patterns Needed
```bash
aget prototype --quick          # Rapid prototype mode
aget release --internal         # Dog-food release
aget release --canary          # Canary deployment
aget metrics --velocity        # Track development speed
```

## Permission System Architecture

### Multi-Tier Configuration
Claude Code uses project/user/company tiers, suggesting AGET structure:

```yaml
# .aget/permissions.yml
tiers:
  company:
    allow: ["read:*"]
    deny: ["delete:products"]

  project:
    allow: ["write:workspace/*"]
    inherit: company

  user:
    allow: ["execute:pytest"]
    override: ["delete:tests"]
```

## Feature Innovations to Adopt

### 1. **Interactive UI Elements**
Using Ink framework for rich terminal UX:
- Interactive pills for background tasks
- Drawer animations for context
- Real-time todo lists with toggle

**AGET Implementation**:
```bash
aget ui --interactive todos
aget ui --drawer evolution
aget ui --pills background
```

### 2. **Output Styles**
Claude Code offers different interaction modes:
- **Explanatory**: Educates about choices
- **Learning**: Collaborative, asks user to do small tasks
- **Minimal**: Just the facts

**AGET Pattern**:
```bash
aget style --set explanatory
aget style --set learning
aget style --create custom
```

### 3. **Hooks System**
Custom shell commands for extensibility:

```bash
aget hooks --add pre-extract
aget hooks --add post-evolution
aget hooks --list
```

### 4. **Subagents Architecture**
Specialized agents for different tasks:

```python
# .aget/agents/reviewer.yml
agent:
  type: reviewer
  capabilities:
    - code_review
    - test_validation
  triggers:
    - on: pr_created
    - on: manual
```

## Rapid Prototyping Methodology

### The 20-Prototype Process
1. Start with basic idea
2. Build prototype with AI
3. Test immediately
4. Share for feedback
5. Iterate or pivot
6. Repeat 20x in 2 days

### AGET Prototyping Command
```bash
aget prototype --init "todo feature"
aget prototype --iterate 1 "move to bottom"
aget prototype --iterate 2 "make interactive"
aget prototype --compare 1..5
aget prototype --ship 5
```

## Product Overhang Concept

> "Product overhang means that a model is able to do a specific thing, but the product isn't built in a way that captures this capability"

### AGET Anti-Overhang Strategy
1. **Regular capability audits**
2. **Remove restrictions with each model update**
3. **Delete unnecessary scaffolding**
4. **Expose, don't constrain**

## Self-Improvement Patterns

### Claude Code Builds Claude Code
Since 90% is self-written, AGET should embrace:

```bash
aget self --improve patterns/
aget self --refactor src/
aget self --test-generate
aget self --document
```

### Continuous Simplification
```bash
aget simplify --analyze
aget simplify --suggest
aget simplify --apply
```

## Engineering Team Evolution

### Key Observations
- Engineers still crucial despite AI writing 90% of code
- Focus shifts to architecture, quality, decisions
- Prototyping becomes primary skill
- Iteration speed matters more than initial perfection

### AGET Team Patterns
```yaml
# .aget/team/workflow.yml
workflow:
  prototype:
    iterations: 10+
    timeframe: hours

  review:
    ai_first: true
    human_verify: true

  deployment:
    internal: continuous
    external: daily
```

## Immediate AGET Enhancements

### Priority 1: Prototyping Speed
```bash
aget prototype --rapid       # AI-powered rapid prototyping
aget prototype --compare     # Compare multiple versions
aget prototype --feedback    # Gather team input
```

### Priority 2: Self-Building
```bash
aget self --build           # AGET builds AGET
aget self --test            # Self-testing
aget self --optimize        # Self-optimization
```

### Priority 3: Interactive UX
```bash
aget ui --rich              # Rich terminal UI
aget ui --interactive       # Interactive elements
aget ui --animate           # Animations
```

## Strategic Implications

### 1. **Simplicity Wins**
- Complex architectures lose to simple, model-powered solutions
- AGET's minimal approach validated

### 2. **Speed Over Perfection**
- 20 prototypes better than 1 "perfect" solution
- Rapid iteration enabled by AI

### 3. **Engineers as Orchestrators**
- Not replaced, but role evolved
- Focus on architecture, quality, user experience

## Implementation Roadmap

### Phase 1: Adopt Core Principles (Immediate)
- [ ] Implement rapid prototyping command
- [ ] Add output styles
- [ ] Create self-improvement patterns

### Phase 2: Interactive Features (Q1 2025)
- [ ] Rich terminal UI with Ink-like features
- [ ] Interactive todo system
- [ ] Drawer and pill UI elements

### Phase 3: Advanced Patterns (Q2 2025)
- [ ] Subagents architecture
- [ ] Multi-tier permissions
- [ ] Continuous deployment patterns

## Metrics to Track

Based on Claude Code's success metrics:

1. **Velocity**
   - PRs per engineer per day
   - Prototypes per feature
   - Time to production

2. **Self-Building**
   - % of AGET written by AGET
   - Code deleted per model update
   - Simplification ratio

3. **Adoption**
   - % of team using daily
   - Features discovered by users
   - Time to first value

## Conclusion

Claude Code's architecture strongly validates AGET's design philosophy while suggesting exciting enhancements around rapid prototyping, self-improvement, and interactive UX. The key takeaway: **simplicity, speed, and exposing model capabilities** trump complex architectures.

---

*This document will be updated as we implement these insights into AGET.*