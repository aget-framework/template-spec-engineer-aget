# AGET v2.0 Roadmap - Unified Vision

*Last Updated: 2025-09-24*
*Status: Active Development (Alpha Released)*
*Original Charter: 2025-09-22 (120 hours committed)*
*Framework Evolution: 2025-09-24*

## Vision Statement

AGET v2 delivers both a **practical CLI tool** for configuring AI agents AND a **conceptual framework** for agents that bridge private innovation to public value.

## v2.0 Dual Mission

### Mission 1: CLI Tool (Original Charter - In Progress)
**Help individual developers configure AI coding agents through simple, local, file-based patterns**
- Core Promise: Working config in <60 seconds
- Status: Alpha released with `aget init`, `aget rollback`
- Remaining: Pattern library, migration tools

### Mission 2: Framework (Evolved Vision - New)
**Enable personal agents to become co-creators of community tools**
- Core Promise: Private exploration → Public manifestation
- Status: Conceptualized, ready to implement
- Key Innovation: Agents that create and maintain public products

## Core Breakthroughs

### 1. The CLI Foundation ✅ (Original v2)
- `aget init` - Initialize agent in <60 seconds
- `aget rollback` - Safe rollback mechanism
- `aget apply` - Apply patterns (Phase 2)
- Three-tier degradation (gh/git/filesystem)

### 2. The Naming Revolution 🎯 (New)
- `aget-*` = Framework components
- `*-aget` = Autonomous agents
- No suffix = Traditional tools

### 3. The Vocabulary Breakthrough 🎯 (New)
- `outputs/` = Agent's internal workspace
- `Outputs` = Public products the agent creates/maintains
- `.aget/` = Framework metadata and state

### 4. The Private→Public Bridge 🎯 (New)
- Private exploration in personal agents
- Pattern extraction through bridge tools
- Public manifestation as community value

## Implementation Phases - Unified Plan

### Phase 1: Complete CLI Core (Week 1) 🚧
**Goal**: Finish original v2 charter commitments
**Hours**: ~25 (of 40 allocated)

- [x] Gate 1: Core CLI foundation (alpha released)
- [ ] Gate 2: Pattern library (35 hours)
- [ ] Gate 3: Migration tools
- [ ] Success criteria: <60 second setup

### Phase 2: Framework Documentation (Week 1-2) 🚧
**Goal**: Codify the evolved vision
**Hours**: ~10

- [x] AGET_FRAMEWORK_VISION.md
- [ ] AGET_VOCABULARY.md (outputs vs Outputs)
- [ ] DIRECTORY_STANDARDS.md (tiered templates)
- [ ] ORIGIN_STORY.md (the 90-minute sprint)
- [ ] .aget/ specification

### Phase 3: First Agent with CLI (Week 2) 🎯
**Goal**: Use CLI to create first framework agent
**Hours**: ~15

- [ ] Use `aget init` to create llm-manager-aget
- [ ] Apply standard template pattern
- [ ] Implement OpenAI spend tracking
- [ ] Establish .aget/evolution/ pattern
- [ ] Test CLI + Framework integration

### Phase 4: Bridge Mechanism (Week 3)
**Goal**: Prove private→public extraction
**Hours**: ~20

- [ ] Build bridge tooling (src/bridges/)
- [ ] Extract first Output (llm-cost-optimizer)
- [ ] Create `aget extract` command
- [ ] Document extraction process

### Phase 5: Pattern Library Integration (Week 4)
**Goal**: CLI patterns support framework agents
**Hours**: ~35 (charter commitment)

- [ ] Session patterns for agents
- [ ] Housekeeping patterns for outputs
- [ ] Bridge patterns for extraction
- [ ] Guardian patterns for enhancement

### Phase 6: Polish & Testing (Week 5)
**Goal**: Meet charter quality gates
**Hours**: ~20 (charter commitment)

- [ ] All commands <2 seconds
- [ ] First 5 users onboard successfully
- [ ] Backward compatible with v1
- [ ] Tests on Mac/Linux/Windows

### Phase 7: Ecosystem Launch (Week 6)
**Goal**: Activate the full vision
**Hours**: ~15

- [ ] Rename repos to convention
- [ ] Create Output Registry
- [ ] Open source example agents
- [ ] Announcement: CLI + Framework

## Integration Points

### CLI Supports Framework
- `aget init` creates agent repositories with framework structure
- `aget apply` adds patterns for outputs→Outputs bridging
- `aget extract` (new) pulls public value from agent outputs
- `aget validate` checks both config AND framework compliance

### Framework Uses CLI
- Agents created with `aget init --template standard`
- Pattern library includes bridge patterns
- Evolution capture integrated with rollback
- Directory standards enforced by CLI

## Breaking Changes from v1

### From Charter Commitment
- **v1 scripts**: Continue to work alongside v2
- **Backward compatible**: AGENTS.md format preserved
- **Progressive enhancement**: No forced migration

### From Framework Evolution
- **Naming**: New aget-*/\*-aget convention (optional but recommended)
- **Directory**: Tiered templates (minimal/standard/advanced)
- **Vocabulary**: outputs vs Outputs distinction
- **Concept**: Agents as value creators, not just automation

## Success Metrics

### Charter Commitments (Must Meet)
- [ ] Time to working config: <60 seconds
- [ ] All commands complete in <2 seconds
- [ ] Zero dependencies beyond Python 3.8+
- [ ] Backward compatible with v1
- [ ] First 5 users successfully onboard

### Framework Goals (Aspirational)
- [ ] 3+ agents using framework patterns
- [ ] 1+ public Output extracted from agent
- [ ] Bridge mechanism documented and proven
- [ ] Evolution capture working
- [ ] Agent→Output registry established

## Hours Tracking

**Charter Commitment**: 120 hours total
- Spent: ~19 hours (Gate 1 alpha)
- Remaining: ~101 hours

**Framework Addition**: ~40 hours estimated
- Documentation: 10 hours
- Bridge mechanism: 20 hours
- Integration: 10 hours

**Total v2 Scope**: ~160 hours

## Migration from v1

For existing users of v1:
1. Naming updates are optional but recommended
2. Directory structure can evolve gradually
3. Core functionality remains backward compatible
4. See UPGRADING.md for detailed migration steps

## Key Deliverables

### Documentation
- [x] AGET_FRAMEWORK_VISION.md
- [ ] AGET_VOCABULARY.md
- [ ] DIRECTORY_STANDARDS.md
- [ ] ORIGIN_STORY.md

### Tools
- [ ] Template installer (`aget init`)
- [ ] Bridge extraction tool
- [ ] Evolution capture system
- [ ] Output Registry

### Example Agents
- [ ] llm-manager-aget (cost tracking)
- [ ] datgen-aget (guardian/enhancer)
- [ ] spotify-aget (renamed from agent-music)

## Risk Mitigation

- **Complexity**: Start with minimal template, evolve as needed
- **Adoption**: Maintain v1 compatibility during transition
- **Scope creep**: Focus on core bridge mechanism first
- **Time**: Each phase has independent value

## Next Immediate Actions

### This Week (Phase 1-2)
1. Complete CLI Gate 2 (pattern library) - Charter commitment
2. Document AGET_VOCABULARY.md - Critical for clarity
3. Test `aget init` creates proper agent structure
4. Begin llm-manager-aget as proof of concept

### Next Week (Phase 3-4)
1. Use CLI to create llm-manager-aget properly
2. Implement OpenAI tracking
3. Build bridge extraction tool
4. Extract first public Output

## Risk Management

### Charter Risks
- **Pattern library complexity**: Start with 5 essential patterns
- **Testing overhead**: Focus on Mac/Linux first
- **User onboarding**: Create video walkthrough

### Framework Risks
- **Scope creep**: Bridge mechanism is MVP only
- **Complexity**: Keep minimal template truly minimal
- **Adoption**: Focus on personal use first

---

*This roadmap unifies the original v2 Charter (CLI tool) with the evolved Framework vision. Both missions reinforce each other: the CLI enables the framework, the framework validates the CLI.*