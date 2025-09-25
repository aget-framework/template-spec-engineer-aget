# AGET v2.0 Release Plan

**Last Updated**: 2025-09-24
**Target Release**: Week of 2025-10-07 (2 weeks)
**Status**: Alpha released, Include Architecture discovered

## Executive Summary

With the breakthrough discovery of the include architecture pattern, we need to integrate this into v2.0 before release. The pattern is proven and will make future updates significantly easier.

## High-Level Roadmap to Release

### Week 1: Include Architecture Implementation (Sept 25-Oct 1)

#### Day 1-2: Template System Update
- [ ] Create AGENTS_AGET.md master template
- [ ] Update all template types (minimal, standard, advanced, agent, tool, hybrid)
- [ ] Add procedural instructions to AGENTS.md templates
- [ ] Implement version tracking in AGENTS_AGET.md

#### Day 3-4: Init Command Enhancement
- [ ] Add --separate flag to init command
- [ ] Implement file creation logic for separate mode
- [ ] Add backward compatibility for merged mode
- [ ] Create migration helper for existing projects

#### Day 5: Testing & Validation
- [ ] Test all template types with --separate
- [ ] Validate with multiple AI agents (Claude, Codex)
- [ ] Test migration from v1 to v2 with include pattern
- [ ] Document any edge cases discovered

### Week 2: Polish & Release Preparation (Oct 2-7)

#### Day 1-2: Documentation Update
- [ ] Update README.md with include architecture
- [ ] Revise QUICK_START.md for new installation method
- [ ] Create MIGRATION_GUIDE.md for existing projects
- [ ] Update all examples to use procedural instructions

#### Day 3-4: Real Project Validation
- [ ] Migrate agent-music fully to include pattern
- [ ] Test with llm-manager-aget
- [ ] Create fresh project with v2.0
- [ ] Get feedback from 2-3 early users

#### Day 5: Release Preparation
- [ ] Finalize CHANGELOG.md
- [ ] Tag v2.0.0 release
- [ ] Update version numbers
- [ ] Prepare announcement

## Critical Path Items

### Must Have for v2.0
1. ✅ Include architecture with procedural instructions
2. ✅ --separate flag in init command
3. ✅ AGENTS_AGET.md templates for all types
4. ✅ Migration guide for existing projects
5. ✅ Backward compatibility maintained

### Nice to Have
1. ⭐ Auto-update command for AGENTS_AGET.md
2. ⭐ Version checking/notification
3. ⭐ Template customization options
4. ⭐ CI/CD integration examples

### Won't Have (v3.0)
1. ❌ Automatic migration tool
2. ❌ Multi-framework support (CURSOR.md, etc.)
3. ❌ Cloud-based template registry
4. ❌ GUI configuration tool

## Risk Mitigation

### Identified Risks
1. **Include pattern adoption** - Mitigated by clear documentation
2. **Breaking changes** - Mitigated by backward compatibility
3. **Agent compatibility** - Validated with Claude and Codex
4. **User confusion** - Mitigated by examples and guides

### Contingency Plans
- If include pattern fails: Fall back to merged approach
- If timeline slips: Release v2.0-rc1 for early feedback
- If major issues found: Delay 1 week for fixes

## Success Criteria

### Technical
- [ ] All tests passing (100+ tests)
- [ ] Include pattern works with 3+ AI agents
- [ ] Migration completes in <5 minutes
- [ ] No breaking changes for v1 users

### Adoption
- [ ] 5+ successful migrations in first week
- [ ] Positive feedback from early users
- [ ] Clear understanding of include pattern
- [ ] Reduced support questions vs v1

## Release Checklist

### Pre-Release
- [ ] All tests passing
- [ ] Documentation complete
- [ ] Migration guide tested
- [ ] Version numbers updated
- [ ] CHANGELOG.md finalized

### Release Day
- [ ] Tag v2.0.0 in git
- [ ] Update main branch
- [ ] Push to GitHub
- [ ] Create GitHub release
- [ ] Announce on relevant channels

### Post-Release
- [ ] Monitor for issues
- [ ] Respond to feedback
- [ ] Plan v2.1 improvements
- [ ] Update roadmap for v3

## Documentation Updates Required

### Critical Updates
1. **README.md** - Add include architecture explanation
2. **QUICK_START.md** - Show --separate flag usage
3. **AGENTS.md template** - Add procedural instructions
4. **MIGRATION_GUIDE.md** - Create from scratch

### Secondary Updates
1. **PATTERNS_EXPLAINED.md** - Include pattern details
2. **TROUBLESHOOTING.md** - Common include issues
3. **API_REFERENCE.md** - Document new commands
4. **ROADMAP.md** - Update for v3 planning

## Communication Plan

### Internal
- Daily progress updates in evolution/
- Test results documented
- Decision records (ADRs) for major choices

### External
- Release announcement template
- Migration guide for existing users
- Quick start for new users
- FAQ for common questions

---
*This plan incorporates the include architecture discovery and ensures v2.0 releases with this critical improvement.*