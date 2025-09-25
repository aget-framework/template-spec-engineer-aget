# v2.0 Release Test Plan

## Overview
Before releasing v2.0 on October 7, we need to validate AGET works with real projects. This plan covers testing with 3 projects and finalizing the release.

## Test Projects

### 1. spotify-aget (formerly music-agent) - Primary Test
**Why**: Complex project with existing CLAUDE.md, perfect for migration testing
**Rename**: agent-music → spotify-aget (follows *-aget convention for agents)

### 2. llm-judge - Secondary Test
**Why**: Different project type, tests versatility
**Type**: Tool project (not agent)

### 3. agentic-planner-cli - Final Validation
**Why**: CLI tool, different requirements
**Type**: Hybrid (tool + agent capabilities)

## Detailed Test Plan

### Phase 1: Prepare Test Environment (30 mins)

#### Step 1.1: Create Test Backup
```bash
# Backup all test projects first
cd ~/github
for project in agent-music llm-judge agentic-planner-cli; do
  cp -r $project ${project}-backup-$(date +%Y%m%d)
done
```

#### Step 1.2: Verify AGET v2 is Ready
```bash
cd aget-cli-agent-template
python3 scripts/validate_patterns.py  # Should show 8/8 passing
python3 scripts/aget_housekeeping_protocol.py sanity-check  # Should be OK
```

### Phase 2: Test spotify-aget Migration (45 mins)

#### Step 2.1: Rename and Prepare
```bash
cd ~/github
mv agent-music spotify-aget
cd spotify-aget
git remote set-url origin git@github.com:aget-framework/spotify-aget.git  # If renaming on GitHub
```

#### Step 2.2: Apply AGET v2 Migration
```bash
# Option A: Fresh install (if no customization)
python3 ~/github/aget-cli-agent-template/installer/install.py . --template agent --with-patterns

# Option B: Migration (if has custom CLAUDE.md)
python3 -m aget migrate . --preserve-custom
```

#### Step 2.3: Validate Migration
```bash
# Test core patterns
python3 scripts/aget_session_protocol.py wake
# Should show project status

python3 scripts/aget_session_protocol.py wind-down
# Should preserve session

# Check pattern application
python3 -m aget apply housekeeping/cleanup --dry-run
# Should scan for cleanup targets

# Verify music-specific functionality still works
python3 analyze_playlists.py  # Or whatever main script exists
```

#### Step 2.4: Test Include Architecture
```bash
# AGENTS.md should exist separately from project files
ls -la AGENTS.md CLAUDE.md
# CLAUDE.md should be symlink to AGENTS.md

# Test AI tool compatibility
echo "Test with Claude Code/Cursor to ensure 'wake up' works"
```

#### Step 2.5: Document Issues
Create `MIGRATION_REPORT.md`:
- Migration time: ___ minutes
- Issues encountered:
- Customizations preserved: Yes/No
- Patterns working: X/8
- AI tool compatibility: Pass/Fail

### Phase 3: Test llm-judge (30 mins)

#### Step 3.1: Different Template Type
```bash
cd ~/github/llm-judge

# This is a tool, not agent - use tool template
python3 ~/github/aget-cli-agent-template/installer/install.py . --template tool
```

#### Step 3.2: Validate Tool-Specific Patterns
```bash
# Tool template has different patterns
python3 scripts/aget_session_protocol.py wake
# Should work but show tool-specific status

# Test tool patterns
python3 -m aget apply documentation/check
# Should analyze docs
```

#### Step 3.3: Check Compatibility
- Verify existing functionality intact
- Test with AI coding assistant
- Document in MIGRATION_REPORT.md

### Phase 4: Test agentic-planner-cli (30 mins)

#### Step 4.1: Hybrid Template
```bash
cd ~/github/agentic-planner-cli

# Hybrid = tool + agent capabilities
python3 ~/github/aget-cli-agent-template/installer/install.py . --template hybrid
```

#### Step 4.2: Test Both Aspects
```bash
# Agent patterns
python3 scripts/aget_session_protocol.py wake
python3 scripts/aget_session_protocol.py wind-down

# Tool patterns
python3 -m aget apply bridge/extract_output
# Should find extractable components
```

### Phase 5: Integration Testing (45 mins)

#### Step 5.1: Cross-Project Testing
```bash
# From aget-cli-agent-template, scan all migrated projects
python3 patterns/meta/project_scanner.py ~/github

# Should show:
# - spotify-aget: COMPLETE or SUBSTANTIAL
# - llm-judge: COMPLETE or SUBSTANTIAL
# - agentic-planner-cli: COMPLETE or SUBSTANTIAL
```

#### Step 5.2: Pattern Validation Across Projects
```bash
for project in spotify-aget llm-judge agentic-planner-cli; do
  echo "Testing $project..."
  cd ~/github/$project
  python3 ~/github/aget-cli-agent-template/scripts/validate_patterns.py patterns/
done
```

#### Step 5.3: AI Tool Testing
Test each project with:
- Claude Code: "wake up" command
- Cursor: Load project, test patterns
- Aider: Verify .aider.conf.yml works

### Phase 6: Release Decision (30 mins)

#### Step 6.1: Create Release Checklist
```markdown
## v2.0 Release Checklist

### Quality Gates
- [ ] All 8 core patterns pass validation
- [ ] 3+ real projects successfully migrated
- [ ] <60 second setup achieved
- [ ] Backward compatibility maintained
- [ ] Migration guide tested and working

### Test Results
- [ ] spotify-aget: ___/10 success
- [ ] llm-judge: ___/10 success
- [ ] agentic-planner-cli: ___/10 success

### Documentation
- [ ] GET_STARTED.md accurate
- [ ] MIGRATE_TO_V2.md tested
- [ ] TROUBLESHOOTING.md covers known issues
- [ ] Release notes prepared

### Release Approval
- [ ] No critical bugs found
- [ ] Performance acceptable
- [ ] User experience smooth
- [ ] GO/NO-GO Decision: _____
```

#### Step 6.2: Fix Critical Issues
If issues found:
1. Fix in aget-cli-agent-template
2. Re-test affected projects
3. Update migration guide

#### Step 6.3: Prepare Release
```bash
cd ~/github/aget-cli-agent-template

# Update version
echo "2.0.0" > .aget/version.json

# Create release notes
cat > RELEASE_NOTES_V2.md << EOF
# AGET v2.0 Release Notes

## What's New
- Pattern-based architecture
- Include architecture (AGENTS.md separate)
- Enhanced CLI commands
- 3 template types (agent, tool, hybrid)

## Migration
See MIGRATE_TO_V2.md for upgrade instructions

## Tested With
- spotify-aget (complex agent)
- llm-judge (tool project)
- agentic-planner-cli (hybrid)
EOF

# Commit release prep
git add -A
git commit -m "release: Prepare v2.0.0

- Tested with 3 real projects
- All quality gates passed
- Migration guide validated"
```

### Phase 7: Release or Delay Decision

#### Option A: RELEASE (if all tests pass)
```bash
# Push to GitHub
git push origin main

# Create release tag
git tag -a v2.0.0 -m "Release v2.0.0: Pattern-based architecture"
git push origin v2.0.0

# Create GitHub release
gh release create v2.0.0 \
  --title "v2.0.0: Pattern-Based Architecture" \
  --notes-file RELEASE_NOTES_V2.md

# Announce
echo "AGET v2.0 released! 🎉"
```

#### Option B: DELAY (if issues found)
```bash
# Document issues
cat > RELEASE_DELAY.md << EOF
# v2.0 Release Delayed

## Critical Issues Found
1. [Issue description]
2. [Issue description]

## New Target Date
October 14, 2025 (1 week delay)

## Fix Plan
- [ ] Fix issue 1
- [ ] Fix issue 2
- [ ] Re-test all projects
EOF

# Create fix branch
git checkout -b fix/v2-blockers
```

## Success Criteria

### Must Have (Release Blockers)
- ✅ Core patterns working (wake, wind-down, sign-off)
- ✅ At least 2/3 test projects migrate successfully
- ✅ No data loss during migration
- ✅ AI tools recognize AGENTS.md

### Should Have (Quality)
- ✅ All 8 patterns pass validation
- ✅ <60 second setup time
- ✅ Clean migration reports
- ✅ No regression in functionality

### Nice to Have (Polish)
- ✅ All 3 projects migrate perfectly
- ✅ Pattern coverage >80%
- ✅ Comprehensive troubleshooting docs
- ✅ Video tutorial ready

## Timeline

### September 25-30
- Test with spotify-aget
- Fix any critical issues
- Update documentation

### October 1-6
- Test with llm-judge and agentic-planner-cli
- Integration testing
- Release preparation

### October 7
- Final go/no-go decision
- Release v2.0 or document delay

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Migration breaks projects | Backup everything first |
| Patterns don't work | Test each individually |
| AI tools don't recognize | Test with each tool |
| Performance issues | Profile and optimize |

---

*Test Plan Created: September 25, 2025*
*Release Target: October 7, 2025*