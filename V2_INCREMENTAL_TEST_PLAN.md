# V2.0 Incremental Test Plan - Daily Execution Guide

## Overview
This incremental plan breaks down the v2.0 release testing into manageable daily chunks, with clear checkpoints and rollback points.

## Phase 1: Environment Preparation (Day 1 - Sept 25)
**Time Estimate**: 1 hour
**Risk Level**: Low

### Morning Tasks (30 min)
- [ ] **1.1** Verify AGET v2 readiness
  ```bash
  cd ~/github/aget-cli-agent-template
  python3 scripts/validate_patterns.py
  python3 scripts/aget_housekeeping_protocol.py sanity-check
  python3 -m pytest tests/ -v --tb=short
  ```
  **Success Criteria**: All validations pass

- [ ] **1.2** Create project backups
  ```bash
  cd ~/github
  for project in agent-music llm-judge agentic-planner-cli; do
    if [ -d "$project" ]; then
      cp -r $project ${project}-backup-20250925
      echo "✅ Backed up $project"
    fi
  done
  ```
  **Success Criteria**: All backups created

### Afternoon Tasks (30 min)
- [ ] **1.3** Create private test repositories
  ```bash
  # Create llm-judge-aget (private fork)
  cd ~/github
  if [ -d "llm-judge" ]; then
    cp -r llm-judge llm-judge-aget
    cd llm-judge-aget
    rm -rf .git
    git init
    git add .
    git commit -m "Initial copy from llm-judge for AGET testing"
  fi

  # Create planner-aget (private copy)
  cd ~/github
  if [ -d "agentic-planner-cli" ]; then
    cp -r agentic-planner-cli planner-aget
    cd planner-aget
    rm -rf .git
    git init
    git add .
    git commit -m "Initial copy from agentic-planner-cli for AGET testing"
  fi
  ```
  **Success Criteria**: Test repos created locally

### Checkpoint 1
- [ ] All backups verified
- [ ] AGET v2 validation passes
- [ ] Test repositories ready
- **If issues**: No changes to original repos, safe to continue

---

## Phase 2: Primary Test - spotify-aget (Day 2 - Sept 26)
**Time Estimate**: 1.5 hours
**Risk Level**: Medium

### Morning Tasks (45 min)
- [ ] **2.1** Prepare spotify-aget (if agent-music exists)
  ```bash
  cd ~/github
  if [ -d "agent-music" ]; then
    mv agent-music spotify-aget
    cd spotify-aget
    git status
  fi
  ```

- [ ] **2.2** Apply AGET v2 migration
  ```bash
  cd ~/github/spotify-aget
  # Check current state first
  ls -la CLAUDE.md AGENTS.md 2>/dev/null

  # Apply AGET
  python3 ~/github/aget-cli-agent-template/installer/install.py . \
    --template agent --with-patterns
  ```
  **Success Criteria**: Installation completes without errors

### Afternoon Tasks (45 min)
- [ ] **2.3** Test core patterns
  ```bash
  cd ~/github/spotify-aget

  # Test each core pattern
  python3 scripts/aget_session_protocol.py wake
  echo "Wake protocol: OK/FAIL"

  python3 scripts/aget_session_protocol.py wind-down
  echo "Wind-down protocol: OK/FAIL"

  python3 scripts/aget_housekeeping_protocol.py housekeeping --dry-run
  echo "Housekeeping: OK/FAIL"
  ```

- [ ] **2.4** Create migration report
  ```bash
  cat > MIGRATION_REPORT.md << 'EOF'
  # spotify-aget Migration Report
  Date: $(date)

  ## Results
  - Migration time: ___ minutes
  - Patterns working: ___/8
  - Custom content preserved: Yes/No
  - Issues found:
    1.
    2.

  ## AI Tool Compatibility
  - [ ] Claude Code: wake command works
  - [ ] Project loads correctly
  - [ ] No errors on startup
  EOF
  ```

### Checkpoint 2
- [ ] Core patterns (wake, wind-down) working
- [ ] No data loss
- [ ] Original functionality preserved
- **If critical issues**: Restore from backup, document problems

---

## Phase 3: Secondary Tests (Day 3 - Sept 27)
**Time Estimate**: 1 hour
**Risk Level**: Low

### Morning Tasks (30 min)
- [ ] **3.1** Test llm-judge-aget with tool template
  ```bash
  cd ~/github/llm-judge-aget

  # Apply tool template (different from agent)
  python3 ~/github/aget-cli-agent-template/installer/install.py . \
    --template tool --with-patterns

  # Quick validation
  python3 scripts/aget_session_protocol.py wake
  python3 -m aget list
  ```
  **Success Criteria**: Tool patterns appropriate for project type

### Afternoon Tasks (30 min)
- [ ] **3.2** Test planner-aget with hybrid template
  ```bash
  cd ~/github/planner-aget

  # Apply hybrid template (agent + tool)
  python3 ~/github/aget-cli-agent-template/installer/install.py . \
    --template hybrid --with-patterns

  # Test both aspects
  python3 scripts/aget_session_protocol.py wake
  python3 -m aget apply documentation/check
  ```
  **Success Criteria**: Both agent and tool patterns work

### Checkpoint 3
- [ ] 3 different templates tested
- [ ] Each template appropriate for project type
- [ ] No conflicts or errors
- **If issues**: Document template-specific problems

---

## Phase 4: Integration Testing (Day 4 - Sept 28)
**Time Estimate**: 1 hour
**Risk Level**: Low

### Morning Tasks (30 min)
- [ ] **4.1** Cross-project scanning
  ```bash
  cd ~/github/aget-cli-agent-template

  # Scan all test projects
  for project in spotify-aget llm-judge-aget planner-aget; do
    if [ -d "../$project" ]; then
      echo "Scanning $project..."
      python3 -m aget validate ../$project
    fi
  done
  ```

### Afternoon Tasks (30 min)
- [ ] **4.2** Performance testing
  ```bash
  # Time critical operations
  cd ~/github/spotify-aget
  time python3 scripts/aget_session_protocol.py wake
  # Should be <2 seconds

  cd ~/github/aget-cli-agent-template
  time python3 -m aget init /tmp/test-quick --template minimal
  # Should be <60 seconds
  ```

### Checkpoint 4
- [ ] All projects validate successfully
- [ ] Performance targets met (<2s commands, <60s setup)
- [ ] Integration issues documented

---

## Phase 5: Fix Critical Issues (Day 5-6 - Sept 29-30)
**Time Estimate**: Variable
**Risk Level**: Medium

### Priority 1: Blockers
- [ ] Fix any data loss issues
- [ ] Fix pattern execution failures
- [ ] Fix AI tool recognition problems

### Priority 2: Quality
- [ ] Fix performance issues
- [ ] Update documentation for found issues
- [ ] Improve error messages

### Priority 3: Polish
- [ ] Clean up migration reports
- [ ] Update troubleshooting guide
- [ ] Prepare demo video

---

## Phase 6: Release Preparation (Day 7-8 - Oct 1-2)
**Time Estimate**: 2 hours
**Risk Level**: Low

### Documentation Tasks
- [ ] **6.1** Update CHANGELOG.md
- [ ] **6.2** Create RELEASE_NOTES_v2.0.md
- [ ] **6.3** Update README.md version references
- [ ] **6.4** Verify all docs accurate

### Technical Tasks
- [ ] **6.5** Update version in aget/__init__.py
- [ ] **6.6** Tag release candidate: v2.0.0-rc1
- [ ] **6.7** Final test run on all patterns
- [ ] **6.8** Create release branch

---

## Phase 7: Final Validation (Day 9-10 - Oct 3-4)
**Time Estimate**: 2 hours
**Risk Level**: Low

### Fresh Install Test
- [ ] **7.1** Test on clean system
  ```bash
  # Create completely fresh test
  mkdir /tmp/fresh-test
  cd /tmp/fresh-test
  git clone https://github.com/aget-framework/aget-cli-agent-template.git
  cd aget-cli-agent-template
  python3 -m aget init ../test-project --template agent --with-patterns
  ```

### Release Checklist
- [ ] **7.2** Complete final checklist
  - [ ] All patterns validated
  - [ ] 3+ projects tested
  - [ ] <60 second setup confirmed
  - [ ] Backward compatibility verified
  - [ ] No critical bugs remain

---

## Phase 8: Release Decision (Day 11-12 - Oct 5-6)
**Time Estimate**: 1 hour
**Risk Level**: High

### Go Decision Criteria
✅ All MUST HAVE criteria met:
- Core patterns working
- No data loss
- AI tools recognize AGENTS.md
- At least 2/3 projects successful

### No-Go Decision Criteria
❌ Any of these present:
- Data loss during migration
- Core patterns failing
- AI tools don't recognize config
- Performance regression >50%

### Release Day (Oct 7)
- [ ] **8.1** Final go/no-go decision
- [ ] **8.2** Push v2.0.0 tag
- [ ] **8.3** Create GitHub release
- [ ] **8.4** Announce release

---

## Daily Status Template
```markdown
## Day X Status - [Date]

### Completed
- ✅ Task 1
- ✅ Task 2

### Issues Found
- 🐛 Issue 1: [description]
- 🐛 Issue 2: [description]

### Next Steps
- [ ] Tomorrow's priority 1
- [ ] Tomorrow's priority 2

### Go/No-Go Status: [GREEN/YELLOW/RED]
```

## Rollback Plan
At any checkpoint, if critical issues:
1. Stop testing immediately
2. Document issues in RELEASE_BLOCKERS.md
3. Restore from backups if needed
4. Create fix branch
5. Re-plan release date

## Success Metrics Dashboard
```
┌────────────────────────────────┐
│ V2.0 Release Readiness         │
├────────────────────────────────┤
│ Patterns Working:     ___/8    │
│ Projects Tested:      ___/3    │
│ Setup Time:          ___sec    │
│ Critical Bugs:       ___       │
│ Go/No-Go:           ____       │
└────────────────────────────────┘
```

---
*Plan Created: September 25, 2025*
*Target Release: October 7, 2025*
*Daily checkpoint times: 10am and 4pm*