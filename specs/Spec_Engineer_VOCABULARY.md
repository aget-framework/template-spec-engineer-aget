# Spec_Engineer Domain Vocabulary

**Version**: 1.0.0
**Status**: Active
**Owner**: template-spec-engineer-aget
**Created**: 2026-01-10
**Scope**: Template vocabulary (DRIVES instance behavior per L481)
**Archetype**: Spec_Engineer

---

## Meta

```yaml
vocabulary:
  meta:
    domain: "specification"
    version: "1.0.0"
    owner: "template-spec-engineer-aget"
    created: "2026-01-10"
    theoretical_basis:
      - "L481: Ontology-Driven Agent Creation"
      - "L482: Executable Ontology - SKOS+EARS Grounding"
    archetype: "Spec_Engineer"
```

---

## Concept Scheme

```yaml
Spec_Engineer_Vocabulary:
  skos:prefLabel: "Spec Engineer Vocabulary"
  skos:definition: "Vocabulary for spec engineer domain agents"
  skos:hasTopConcept:
    - Spec_Engineer_Core_Concepts
  rdf:type: skos:ConceptScheme
```

---

## Core Concepts

### Requirement

```yaml
Requirement:
  skos:prefLabel: "Requirement"
  skos:definition: "A documented need that a system must satisfy"
  skos:broader: Spec_Engineer_Core_Concepts
  skos:inScheme: Spec_Engineer_Vocabulary
```

### EARS_Pattern

```yaml
EARS_Pattern:
  skos:prefLabel: "EARS Pattern"
  skos:definition: "Easy Approach to Requirements Syntax - structured requirement format"
  skos:broader: Spec_Engineer_Core_Concepts
  skos:inScheme: Spec_Engineer_Vocabulary
```

### Capability

```yaml
Capability:
  skos:prefLabel: "Capability"
  skos:definition: "A discrete function or behavior the system provides"
  skos:broader: Spec_Engineer_Core_Concepts
  skos:inScheme: Spec_Engineer_Vocabulary
```

### Constraint

```yaml
Constraint:
  skos:prefLabel: "Constraint"
  skos:definition: "A limitation or restriction on system design or behavior"
  skos:broader: Spec_Engineer_Core_Concepts
  skos:inScheme: Spec_Engineer_Vocabulary
```

### Verification

```yaml
Verification:
  skos:prefLabel: "Verification"
  skos:definition: "Process of confirming requirement satisfaction"
  skos:broader: Spec_Engineer_Core_Concepts
  skos:inScheme: Spec_Engineer_Vocabulary
```

---

## Extension Points

Instances extending this template vocabulary should:
1. Add domain-specific terms under appropriate broader concepts
2. Maintain SKOS compliance (prefLabel, definition, broader/narrower)
3. Reference foundation L-docs where applicable
4. Use `research_status` for terms under investigation

---

## References

- L481: Ontology-Driven Agent Creation
- L482: Executable Ontology - SKOS+EARS Grounding
- R-REL-015: Template Ontology Conformance
- AGET_VOCABULARY_SPEC.md

---

*Spec_Engineer_VOCABULARY.md v1.0.0 — SKOS-compliant template vocabulary*
*Generated: 2026-01-10*
