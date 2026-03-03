# Template: Spec-Engineer Agent

> Transform requirements into formal specifications using EARS methodology

**Version**: v3.7.0 | **Archetype**: Spec-Engineer | **Skills**: 2 specialized + 15 universal

---

## Why Spec-Engineer?

The Spec-Engineer archetype brings **requirements engineering rigor** to specification work. Unlike informal documentation, spec-engineer agents provide:

- **Spec validation** — Check specifications for ambiguity, completeness, and testability
- **Requirement generation** — Transform informal needs into formal EARS-pattern requirements
- **Traceability** — Connect requirements to implementation with verifiable links

**For evaluators**: If you need an AI that can formalize requirements into aerospace-grade specifications, the Spec-Engineer archetype brings EARS methodology to your requirements process.

**Domain knowledge that compounds**: Spec-engineer agents build persistent understanding of your requirements landscape — specification patterns, domain terminology, and validation criteria. Unlike tools that start fresh each session, your agent accumulates specification context that makes each requirement more precise and each validation more thorough.

---

## Skills

Spec-Engineer agents come with **2 archetype-specific skills** plus the universal AGET skills.

### Archetype Skills

| Skill | Description |
|-------|-------------|
| **aget-validate-spec** | Validate specifications for ambiguity, completeness, and testability. Identifies gaps and conflicts. |
| **aget-generate-requirement** | Generate formal requirements using EARS patterns (ubiquitous, event-driven, state-driven, optional-feature). |

### Universal Skills

All AGET agents include session management, knowledge capture, and health monitoring:

- `aget-wake-up` / `aget-wind-down` — Session lifecycle
- `aget-create-project` / `aget-review-project` — Project management
- `aget-record-lesson` / `aget-capture-observation` — Learning capture
- `aget-check-health` / `aget-check-kb` / `aget-check-evolution` — Health monitoring
- `aget-propose-skill` / `aget-create-skill` — Skill development
- `aget-save-state` / `aget-file-issue` — State and issue management

---

## Ontology

Spec-Engineer agents use a **formal vocabulary** of 7 concepts organized into 2 clusters:

| Cluster | Concepts |
|---------|----------|
| **Requirements** | Requirement, Capability, Constraint |
| **EARS Patterns** | EARS_Pattern, Trigger, Response, Rationale |

This vocabulary enables precise communication about specifications.

See: [`ontology/ONTOLOGY_spec_engineer.yaml`](ontology/ONTOLOGY_spec_engineer.yaml)

---

## Quick Start

```bash
# 1. Clone the template
git clone https://github.com/aget-framework/template-spec-engineer-aget.git my-spec-engineer-agent
cd my-spec-engineer-agent

# 2. Configure identity
# Edit .aget/version.json:
#   "agent_name": "my-spec-engineer-agent"
#   "domain": "your-domain"

# 3. Verify setup
python3 -m pytest tests/ -v
# Expected: All tests passing
```

### Try the Skills

```bash
# In Claude Code CLI
/aget-validate-spec         # Check a specification
/aget-generate-requirement  # Create EARS requirement
```

---

## What Makes Spec-Engineer Different

| Aspect | Informal Docs | Spec-Engineer Agent |
|--------|--------------|---------------------|
| **Requirements** | Ambiguous prose | EARS-pattern formal statements |
| **Validation** | Human intuition | Systematic ambiguity detection |
| **Testability** | Hoped for | Verified at specification time |
| **Patterns** | Ad-hoc | Ubiquitous, event-driven, state-driven |
| **Domain memory** | Starts fresh each session | Accumulates specification expertise over time |

---

## .claude/ Directory

| Directory | Purpose | Owner |
|-----------|---------|-------|
| `.claude/skills/` | Slash command definitions | Framework + Agent |
| `.claude/agents/` | Subagent definitions | Agent |
| `.claude/rules/` | Path-scoped context rules | Agent |

Skills are provided by the template. Agents and rules directories are scaffolded for your customization.

---

## Framework Specification

| Attribute | Value |
|-----------|-------|
| **Framework** | [AGET v3.7.0](https://github.com/aget-framework/aget) |
| **Archetype** | Spec-Engineer |
| **Skills** | 17 total (2 archetype + 15 universal) |
| **Ontology** | 7 concepts, 2 clusters |
| **License** | Apache 2.0 |

---

## Learn More

- **[AGET Framework](https://github.com/aget-framework/aget)** — Core framework documentation
- **[Archetype Guide](https://github.com/aget-framework/aget/blob/main/docs/GETTING_STARTED.md)** — All 12 archetypes explained
- **[Getting Started](https://github.com/aget-framework/aget/blob/main/docs/GETTING_STARTED.md)** — Full onboarding guide

---

## Related Archetypes

| Archetype | Best For |
|-----------|----------|
| **[Architect](https://github.com/aget-framework/template-architect-aget)** | System design driving specs |
| **[Developer](https://github.com/aget-framework/template-developer-aget)** | Implementing specs |
| **[Reviewer](https://github.com/aget-framework/template-reviewer-aget)** | Validating spec compliance |

---

**AGET Framework** | Apache 2.0 | [Issues](https://github.com/aget-framework/template-spec-engineer-aget/issues)
