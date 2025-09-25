# Day 1 Test Plan - Environment Preparation
**Date**: September 25, 2025
**Duration**: 1 hour total
**Risk Level**: Low
**Prerequisites**: Access to aget-cli-agent-template and target projects

## Morning Session (10:00 AM - 10:30 AM)

### Task 1.1: Verify AGET v2 Readiness (10 minutes)

First, ensure AGET v2 is working correctly:

```bash
# Navigate to AGET repository
cd ~/github/aget-cli-agent-template

# Run validation script - should show 8/8 patterns passing
python3 scripts/validate_patterns.py

# Check system health - should report OK
python3 scripts/aget_housekeeping_protocol.py sanity-check

# Run test suite - should have >80% coverage
python3 -m pytest tests/ -v --tb=short

# Quick CLI test - should complete in <2 seconds
python3 -m aget list
```

**Expected Output**:
- ✅ Pattern validation: 8/8 patterns valid
- ✅ System check: Status OK
- ✅ Tests: All passing (or known failures documented)
- ✅ CLI: Commands respond in <2 seconds

**Troubleshooting**:
- If patterns fail: Check for syntax errors in patterns/*.py
- If system check fails: Verify Python 3.8+ installed
- If tests fail: Review specific test output, may be environment-specific

### Task 1.2: Create Project Backups (20 minutes)

Create safety backups before any modifications:

```bash
cd ~/github

# Create dated backup directory
mkdir -p backups/20250925

# Backup each project if it exists
for project in agent-music spotify-aget llm-judge agentic-planner-cli; do
    if [ -d "$project" ]; then
        echo "Backing up $project..."
        cp -r "$project" "backups/20250925/${project}-backup"

        # Verify backup
        if [ -d "backups/20250925/${project}-backup" ]; then
            echo "✅ Successfully backed up $project"
            # Quick size check
            du -sh "backups/20250925/${project}-backup"
        else
            echo "❌ Failed to backup $project"
        fi
    else
        echo "⏭️ Skipping $project (not found)"
    fi
done

# List all backups
echo -e "\n📁 Backup Summary:"
ls -la backups/20250925/
```

**Checkpoint**: Verify all existing projects have backups before proceeding

## Afternoon Session (4:00 PM - 4:30 PM)

### Task 1.3: Create Private Test Repositories (30 minutes)

Create isolated test environments:

#### Step A: Create llm-judge-aget (if llm-judge exists)

```bash
cd ~/github

if [ -d "llm-judge" ]; then
    echo "Creating llm-judge-aget test repository..."

    # Create copy
    cp -r llm-judge llm-judge-aget
    cd llm-judge-aget

    # Initialize as new git repo (removes history for privacy)
    rm -rf .git
    git init

    # Create initial commit
    git add .
    git commit -m "Initial copy from llm-judge for AGET v2 testing

    - Testing tool template compatibility
    - Private repository for safe experimentation
    - Original at ~/github/backups/20250925/llm-judge-backup"

    echo "✅ Created llm-judge-aget"

    # Document current state
    echo "Project structure:"
    ls -la

    # Check for existing agent configs
    if [ -f "CLAUDE.md" ]; then
        echo "📝 Found existing CLAUDE.md ($(wc -l < CLAUDE.md) lines)"
    fi
    if [ -f "AGENTS.md" ]; then
        echo "📝 Found existing AGENTS.md ($(wc -l < AGENTS.md) lines)"
    fi
else
    echo "⏭️ llm-judge not found, skipping"
fi
```

#### Step B: Create planner-aget (if agentic-planner-cli exists)

```bash
cd ~/github

if [ -d "agentic-planner-cli" ]; then
    echo "Creating planner-aget test repository..."

    # Create copy
    cp -r agentic-planner-cli planner-aget
    cd planner-aget

    # Initialize as new git repo
    rm -rf .git
    git init

    # Create initial commit
    git add .
    git commit -m "Initial copy from agentic-planner-cli for AGET v2 testing

    - Testing hybrid template compatibility
    - Private repository for safe experimentation
    - Original at ~/github/backups/20250925/agentic-planner-cli-backup"

    echo "✅ Created planner-aget"

    # Document current state
    echo "Project structure:"
    ls -la

    # Check for existing configs
    for config in CLAUDE.md AGENTS.md .cursorrules .aider.conf.yml; do
        if [ -f "$config" ]; then
            echo "📝 Found $config"
        fi
    done
else
    echo "⏭️ agentic-planner-cli not found, skipping"
fi
```

#### Step C: Verify Test Environment

```bash
cd ~/github

echo -e "\n🧪 Test Environment Summary:"
echo "=========================="

# Check what we have
for repo in spotify-aget llm-judge-aget planner-aget; do
    if [ -d "$repo" ]; then
        echo "✅ $repo - ready for testing"
        cd "$repo"
        git log --oneline -1 2>/dev/null || echo "   (not git initialized)"
        cd ..
    else
        echo "❌ $repo - not created"
    fi
done

# Verify backups
echo -e "\n💾 Backup Verification:"
ls -lh backups/20250925/ 2>/dev/null || echo "No backups found"

# Final readiness check
echo -e "\n🚦 Readiness Status:"
if [ -d "aget-cli-agent-template" ] && [ -d "backups/20250925" ]; then
    echo "✅ Ready for Day 2 testing"
else
    echo "⚠️ Issues found - review above output"
fi
```

## Day 1 Completion Checklist

### Morning Session ✓
- [ ] AGET validation passed (8/8 patterns)
- [ ] System health check OK
- [ ] Test suite running
- [ ] All existing projects backed up to backups/20250925/

### Afternoon Session ✓
- [ ] llm-judge-aget created (or skipped if not applicable)
- [ ] planner-aget created (or skipped if not applicable)
- [ ] All test repos initialized with git
- [ ] Original configs documented

### End of Day Status Report

```markdown
## Day 1 Status - September 25, 2025

### ✅ Completed
- AGET v2 validation: [PASS/FAIL]
- Backups created: [#] projects
- Test repos created: [#] repos

### 🐛 Issues Found
- Issue 1: [description or "None"]
- Issue 2: [description or "None"]

### 📋 Ready for Day 2
- [ ] spotify-aget (or agent-music) available
- [ ] llm-judge-aget ready (optional)
- [ ] planner-aget ready (optional)
- [ ] AGET v2 validated and working

### 🚦 Go/No-Go Status: [GREEN/YELLOW/RED]
- GREEN = Ready for Day 2
- YELLOW = Minor issues, can proceed with caution
- RED = Blocking issues, need resolution first

### Notes for Day 2:
[Any specific observations or preparations needed]
```

## Rollback Instructions (If Needed)

If any critical issues occur:

```bash
# Restore from backup
cd ~/github
rm -rf llm-judge-aget planner-aget  # Remove test repos
cp -r backups/20250925/[project]-backup ./[project]  # Restore original

# Document the issue
cat >> DAY_1_ISSUES.md << EOF
Issue Time: $(date)
Issue: [description]
Impact: [what failed]
Resolution: [rolled back / fixed / pending]
EOF
```

---
*Day 1 Plan - Environment Preparation*
*Safe, reversible setup with multiple checkpoints*