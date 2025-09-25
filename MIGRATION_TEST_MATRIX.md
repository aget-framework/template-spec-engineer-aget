# AGET v2.0 Migration Test Matrix

## Test Strategy
Test different project types, templates, and migration scenarios to ensure v2.0 works universally.

## Projects Ready for Testing

### 1. ✅ spotify-aget (Completed)
- **Type**: Complex music analysis agent
- **Template Used**: advanced
- **Status**: SUCCESS (after script fix)
- **Customization**: Heavy (99-line CLAUDE.md)

### 2. 🔄 llm-judge-aget (Ready)
- **Type**: Tool/Library project
- **Template**: Should use `standard` (tool-focused)
- **Existing Structure**: src/, tests/, pyproject.toml
- **Expected Issues**: Different directory structure

### 3. 🔄 planner-aget (Ready)
- **Type**: CLI tool
- **Template**: Should use `standard` or `minimal`
- **Existing Structure**: Flat Python files
- **Expected Issues**: No src/ directory

### 4. 🔄 aget-cli-agent-template (Self-test)
- **Type**: The framework itself
- **Template**: Should already have everything
- **Test**: Ensure it can update itself

### 5. 🔄 New Project Test
- **Type**: Fresh project
- **Template**: Test all three (minimal, standard, advanced)
- **Test**: Clean installation

## Migration Test Checklist

### Quick Test Sequence (Per Project)
```bash
# 1. Navigate and check current state
cd ~/github/[project-name]
ls -la CLAUDE.md AGENTS.md 2>/dev/null
git status

# 2. Apply AGET v2
python3 ~/github/aget-cli-agent-template/installer/install.py . --template [template]
cp -r ~/github/aget-cli-agent-template/patterns .
cp ~/github/aget-cli-agent-template/scripts/aget_*.py scripts/

# 3. Quick validation
python3 scripts/aget_session_protocol.py wake
python3 scripts/aget_housekeeping_protocol.py sanity-check
python3 scripts/aget_session_protocol.py wind-down

# 4. Check compatibility
ls -la AGENTS.md CLAUDE.md
cat AGENTS.md | head -20
```

## Test Execution Plan

### Test A: llm-judge-aget (Tool Project)
```bash
cd ~/github/llm-judge-aget

# Pre-check
echo "=== PRE-MIGRATION STATE ==="
ls -la *.md
find . -name "*.py" -type f | head -5

# Migrate with standard template
python3 ~/github/aget-cli-agent-template/installer/install.py . --template standard

# Add AGET v2 components
cp -r ~/github/aget-cli-agent-template/patterns .
cp ~/github/aget-cli-agent-template/scripts/aget_*.py scripts/
mkdir -p scripts && cp ~/github/aget-cli-agent-template/scripts/*.py scripts/

# Test
python3 scripts/aget_session_protocol.py wake
python3 scripts/aget_session_protocol.py wind-down

# Verify tool still works
python3 -m pytest tests/ -k test_basic -v  # Or whatever test exists
```

### Test B: planner-aget (Simple CLI)
```bash
cd ~/github/planner-aget

# Pre-check
echo "=== PRE-MIGRATION STATE ==="
ls -la
python3 main.py --help 2>/dev/null || echo "No main.py"

# Migrate with minimal template
python3 ~/github/aget-cli-agent-template/installer/install.py . --template minimal

# Add patterns
cp -r ~/github/aget-cli-agent-template/patterns .
mkdir -p scripts && cp ~/github/aget-cli-agent-template/scripts/aget_*.py scripts/

# Test
python3 scripts/aget_session_protocol.py wake
python3 scripts/aget_housekeeping_protocol.py housekeeping --dry-run

# Verify CLI still works
python3 planner.py --help 2>/dev/null || echo "Check main functionality"
```

### Test C: Fresh Project (Multiple Templates)
```bash
# Minimal template
mkdir -p /tmp/test-minimal
cd /tmp/test-minimal
python3 ~/github/aget-cli-agent-template/installer/install.py . --template minimal
python3 scripts/session_protocol.py wake
echo "Minimal: $(ls -la | wc -l) files"

# Standard template
mkdir -p /tmp/test-standard
cd /tmp/test-standard
python3 ~/github/aget-cli-agent-template/installer/install.py . --template standard
python3 scripts/session_protocol.py wake
echo "Standard: $(ls -la | wc -l) files"

# Advanced template
mkdir -p /tmp/test-advanced
cd /tmp/test-advanced
python3 ~/github/aget-cli-agent-template/installer/install.py . --template advanced
python3 scripts/session_protocol.py wake
echo "Advanced: $(ls -la | wc -l) files"
```

### Test D: Re-migration (Idempotent Test)
```bash
cd ~/github/spotify-aget

# Save current state
cp -r scripts scripts.backup

# Re-run migration
python3 ~/github/aget-cli-agent-template/installer/install.py . --template advanced

# Should preserve everything
diff -r scripts scripts.backup || echo "Scripts changed"
python3 scripts/aget_session_protocol.py wake  # Should still work
```

## Expected Results Matrix

| Project | Template | Wake | Wind | House | Docs | Original Function | Grade |
|---------|----------|------|------|-------|------|------------------|-------|
| spotify-aget | advanced | ✅ | ✅ | ✅ | ✅ | ✅ | A |
| llm-judge-aget | standard | ? | ? | ? | ? | ? | ? |
| planner-aget | minimal | ? | ? | ? | ? | ? | ? |
| test-minimal | minimal | ? | ? | ? | ? | N/A | ? |
| test-standard | standard | ? | ? | ? | ? | N/A | ? |
| test-advanced | advanced | ? | ? | ? | ? | N/A | ? |

## Critical Success Factors

### Must Pass (Release Blockers)
- [ ] All projects can wake/wind-down
- [ ] No data loss during migration
- [ ] Original functionality preserved
- [ ] Scripts work after fix

### Should Pass (Quality Gates)
- [ ] All templates install correctly
- [ ] Patterns accessible
- [ ] Documentation grades reasonable
- [ ] Re-migration is safe

### Nice to Have (Polish)
- [ ] Clean directory structure
- [ ] No duplicate files
- [ ] Consistent behavior across templates

## Issues to Track

### Known Issues
1. Installer only has minimal/standard/advanced (no "agent", "tool", "hybrid")
2. --with-patterns flag doesn't work
3. Must manually copy patterns/

### Discovered Issues
- [ ] (Document as we find them)

## Quick Decision Tree

```
If project is:
├── Library/Tool → use "standard" template
├── CLI Application → use "minimal" template
├── Agent/Complex → use "advanced" template
└── Fresh/New → use "minimal" and upgrade as needed
```

---
*Ready to test more migrations beyond spotify-aget*