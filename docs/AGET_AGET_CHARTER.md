# Charter for aget-aget Repository (Reference Laboratory)

## Identity
**aget-aget** is the private reference laboratory for AGET framework development, serving as the first adopter and experimentation ground.

## Mission
Validate, experiment, and dogfood AGET framework changes before they impact the broader community.

## What aget-aget IS
- ✅ **Reference Laboratory** - Shows how to run a private AGET lab
- ✅ **First Adopter** - Always running latest/beta versions
- ✅ **Experiment Ground** - Tests risky changes safely
- ✅ **Pattern Incubator** - Develops new patterns before upstream
- ✅ **Dogfooding Example** - Demonstrates "eating your own dogfood"

## What aget-aget IS NOT
- ❌ **Not The Only Lab** - Just one of many possible private labs
- ❌ **Not Required** - Teams can fork without referencing it
- ❌ **Not Authoritative** - Experiments may fail or be abandoned
- ❌ **Not Public Standards** - Those belong in aget-cli-agent-template

## Relationship to aget-cli-agent-template
```
aget-cli-agent-template              aget-aget
(Public Framework)          ←→        (Private Lab)
     ↑                                    ↓
  Stable Patterns                    Experiments
     ↑                                    ↓
  PR if Successful          Try Risky Changes First
```

## Lab Protocols

### Experimentation Flow
1. **Identify Need** - From usage or community feedback
2. **Experiment in aget-aget** - Try multiple approaches
3. **Validate Through Dogfooding** - Use it ourselves first
4. **Document Learnings** - Evolution entries
5. **Upstream if Universal** - PR to template if broadly useful
6. **Keep if Specific** - Retain in lab if too opinionated

### What Stays in aget-aget
- Experimental patterns still being validated
- Opinionated workflows specific to our needs
- Failed experiments (as learning documentation)
- Meta-documentation about AGET itself
- Advanced/complex patterns not ready for general use

### What Moves Upstream
- Patterns that proved universally useful
- Bug fixes discovered through experimentation
- Framework improvements
- Protocol enhancements
- Documentation improvements

## Success Metrics
- Days ahead of stable (how early we catch issues)
- Patterns graduated to upstream
- Issues caught before reaching users
- Experimental learnings documented

## Example Experiments (Past/Current)
- ✅ **Compatibility Checker** - Validated, moved upstream
- 🧪 **Multi-agent Coordination** - Still experimental
- ❌ **Auto-commit on Edit** - Failed, too aggressive
- 🧪 **AI Review Pattern** - Under development

## For Other Private Labs

This charter serves as a template. Your private lab might focus on:
- Security-first patterns (security-aget)
- Data science workflows (ds-aget-lab)
- Enterprise compliance (corp-aget-private)
- Educational patterns (edu-aget-lab)

The beauty: Each lab can have its own charter while following the AGET protocol!

---
*Last Updated: 2025-09-25*
*Charter Version: 1.0*
*Note: This is the charter for THE reference aget-aget, not YOUR aget-aget*