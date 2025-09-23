# AGET v2 Project Plan

**Version**: 1.0
**Date**: 2025-09-22
**Status**: COMMITTED SCOPE
**Total Effort**: ~143 hours
**Timeline**: Flexible
**Strategic Direction**: AGET as future agent suite foundation (config first)

## 1. Executive Summary

### Mission
AGET helps individual developers configure AI coding agents for their projects through simple, local, file-based patterns.

### Core Promise
Transform agent configuration from trial-and-error to predictable patterns in under 60 seconds.

### Strategic Vision
AGET v2 establishes the foundation for a future suite of developer agents:
- **v2.0**: Core configuration tool (this release)
- **v2.x**: Subcommand structure (`aget config`)
- **Future**: Additional agents (`aget track`, `aget gate`, `aget ship`)

This v2 focuses solely on configuration while architecting for future expansion.

### Success Criteria
- Time to working config: <60 seconds
- Zero runtime dependencies
- All commands complete in <2 seconds
- First 5 users successfully onboard without help
- 14 existing projects successfully migrated
- Architecture supports future subcommands without breaking changes

## 2. Naming Decision

### Keep AGET
**Decision**: Retain AGET name
**Rationale**:
- Already established with v1 users
- Short, memorable CLI command
- Allows future evolution to suite
- No migration/rebranding cost

### Future-Ready Architecture
v2.0 commands will map to future structure:
```bash
# v2.0 (current)          # v2.1+ (future)
aget init           →      aget config init
aget validate       →      aget config validate
aget apply          →      aget config apply
```

Internal implementation will support both patterns from day one.

## 3. Formal Vocabulary

### Core Terms

| Term | Definition | Usage Example |
|------|------------|---------------|
| **AGET** | The agent configuration tool (future: suite) | "Run aget init" |
| **Pattern** | Reusable agent configuration template | "Apply the session pattern" |
| **Agent** | AI coding assistant (Claude Code, Cursor, etc.) | "Configure your agent" |
| **Configuration** | The AGENTS.md file content | "Update configuration" |
| **Apply** | Add pattern to existing configuration | "aget apply pattern-name" |
| **Rollback** | Restore previous configuration state | "aget rollback" |
| **Template** | Starting configuration for new projects | "aget init --template basic" |
| **Migration** | Process of updating v1 to v2 format | "aget migrate analyze" |

### Vocabulary Rules
- Use terms consistently in all output
- Never use synonyms in error messages
- Define new terms before first use
- Maintain consistency with future suite terminology

## 4. Scope Definition

### What v2 IS

#### Primary Function
A local CLI tool that:
- Generates AGENTS.md files from templates
- Validates agent configuration syntax
- Suggests patterns based on project type
- Manages configuration versions locally
- Assists with v1→v2 migration
- **Architecturally prepared for future suite expansion**

#### Technical Boundaries
- Runs entirely offline
- Zero external dependencies beyond Python 3.8+
- All state in .aget/ directory
- Configuration via simple JSON
- Total install size under 1MB
- **Subcommand structure ready (but not exposed)**

### What v2 IS NOT (Yet)

#### Not Building in v2.0
- Full agent suite
- track, gate, ship commands
- Distributed orchestration
- Cloud services
- Multi-agent coordination

These are **future possibilities**, not v2.0 scope.

## 5. Implementation Plan

### Phase 1: Core CLI (~48 hours)

#### Deliverables
- Five core commands working
- Template system functional
- Backup mechanism reliable
- Version management (SemVer)
- Environment variable support
- XDG directory compliance
- **Internal subcommand structure (not exposed)**

#### Architecture Decision
```python
# v2.0 internal structure (future-ready)
class AgetCLI:
    def __init__(self):
        self.modules = {
            'config': ConfigModule(),  # All v2.0 functionality
            # Future: 'track': TrackModule(),
            # Future: 'gate': GateModule(),
        }

    def route_command(self, cmd):
        # v2.0: Direct commands
        if cmd in ['init', 'validate', 'apply', 'rollback', 'list']:
            return self.modules['config'].handle(cmd)
        # v2.1+: Subcommands
        elif cmd == 'config':
            return self.modules['config'].handle(subcmd)
```

### Phase 2: Patterns Library (~35 hours)

#### Deliverables
- 10+ validated patterns
- Pattern detection from existing files
- Business rules for compatibility
- Pattern suggestion algorithm

#### Patterns to Include
1. session-management
2. testing-protocols
3. housekeeping
4. documentation
5. business-rules
6. error-handling
7. file-management
8. git-integration
9. environment-config
10. agent-coordination

### Phase 2.5: Migration Assistant (~15 hours)

#### Deliverables
- Project analysis command
- Migration plan generator
- Automated migration execution
- Verification system

#### Test Cases
- Gabor's 14 projects:
  - 3 complete → v2
  - 1 partial → v2
  - 10 not started → v2

### Phase 3: Polish (~20 hours)

#### Deliverables
- Error messages that teach
- Performance optimization
- Cross-platform testing
- Contextual help

### Phase 4: Documentation (~10 hours)

#### Deliverables
- Quick start guide
- Pattern cookbook
- Migration guide
- API reference
- **Future suite hints (subtle)**

### Phase 5: Testing & Validation (~15 hours)

#### Deliverables
- Unit tests for all commands
- Integration tests for workflows
- Cross-platform validation
- User acceptance tests
- **Subcommand routing tests (internal)**

## 6. Go/No-Go Decision Gates & Release Points

### Gate 1: Core CLI Complete → v2.0-alpha
**When**: End of Phase 1
**Release**: v2.0-alpha (internal use)
**Go Criteria**:
- [ ] All 5 commands execute without error
- [ ] Backup/rollback mechanism works
- [ ] <2 second response time
- [ ] Clean error messages
- [ ] Internal routing supports future expansion

### Gate 2: Pattern System Ready → v2.0-beta
**When**: End of Phase 2
**Release**: v2.0-beta (close collaborators)
**Go Criteria**:
- [ ] 10+ patterns validated
- [ ] Conflicts detected correctly
- [ ] Business rules enforced
- [ ] Suggestion algorithm works

### Gate 3: Migration Tested → (Internal Checkpoint)
**When**: End of Phase 2.5
**Release**: None - internal validation only
**Rationale**: Migration tools tested but not released publicly
**Go Criteria**:
- [ ] All 14 projects analyzed
- [ ] Migration plans generated
- [ ] CCB successfully migrated
- [ ] No data loss

### Gate 4: First User Test → v2.0-rc
**When**: Before Phase 5
**Release**: v2.0-rc (release candidate, external testers)
**Go Criteria**:
- [ ] Internal dogfooding successful
- [ ] 60-second onboarding achieved
- [ ] All commands documented
- [ ] Future expansion path validated

### Gate 5: Release Ready → v2.0
**When**: End of Phase 5
**Release**: v2.0 (public release)
**Go Criteria**:
- [ ] 5 external users successful
- [ ] All tests passing
- [ ] No data loss incidents
- [ ] Satisfaction >7/10
- [ ] v2.1 upgrade path clear

## 7. Migration Strategy

### Test Bed: 14 Projects
```
Complete (3):
- aget-cli-agent-template (self)
- [main workspace]
- [other]

Partial (1):
- CCB (60% complete)

Not Started (10):
- GM-RKB
- agent-music
- DatGen
- [others...]
```

### Migration Approach
1. Analyze all projects
2. Create customized plans
3. Test with CCB first
4. Apply to remaining projects
5. Document lessons learned
6. **Validate future suite compatibility**

## 8. Risk Register

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Platform compatibility | Medium | High | Test early on all OS |
| Migration complexity | Medium | High | Start with simplest case |
| Performance >2 seconds | Low | Medium | Profile critical path |
| User confusion | Medium | Medium | Clear vocabulary, examples |
| Scope creep (suite features) | High | High | Strict v2.0 boundaries |
| Future compatibility | Low | High | Architecture review at Gate 1 |

## 9. Future Suite Preparation

### v2.0 Foundations
While not implementing suite features, v2.0 will:
- Use subcommand-ready architecture internally
- Establish shared utilities (logging, config)
- Define consistent patterns (dry-run, rollback)
- Create extensible file structure

### Post-v2.0 Roadmap
```
v2.1: Expose subcommand structure
      aget config init (backward compatible)

v2.x: Add first companion
      aget track todos

v3.0: Full suite
      aget config / track / gate / ship
```

### File Structure (Future-Ready)
```
aget/
├── __main__.py      # Main entry, routes to modules
├── config/          # All v2.0 functionality
│   ├── commands/
│   └── patterns/
├── shared/          # Future shared utilities
│   ├── logging.py
│   └── backup.py
└── future/          # Placeholder for suite
    ├── track/       # (not in v2.0)
    ├── gate/        # (not in v2.0)
    └── ship/        # (not in v2.0)
```

## 10. Success Metrics

### Quantitative (v2.0)
- Onboarding time: <60 seconds
- Command response: <2 seconds
- Migration success: >95%
- User satisfaction: >7/10
- Test coverage: >80%

### Qualitative (Future-Ready)
- Architecture supports suite expansion
- No breaking changes needed for v2.1
- Clear extension points identified
- Shared patterns established

## 11. Communication Strategy

### v2.0 Messaging
- Focus: Configuration tool that works
- Mention: "Foundation for future capabilities"
- Avoid: Over-promising suite features

### Documentation Hints
```markdown
Note: AGET is designed to grow with your needs.
Future versions may include additional developer tools.
```

## 12. The Journey

### v2.0: Ship Value Now
- Solves immediate configuration problem
- Establishes AGET brand
- Proves core concept

### v2.x: Gradual Enhancement
- Add features as needed
- Maintain backward compatibility
- Let user needs drive expansion

### v3.0: The Suite (If Warranted)
- Only if users want it
- Only if v2 succeeds
- Only if value is clear

---

**Commitment**: We commit to delivering v2.0 as specified, with architecture that enables (but doesn't require) future expansion.

**Philosophy**: Build the tool needed today, with room for tomorrow.

**Next Step**: Run project scanner for baseline (Step 2)