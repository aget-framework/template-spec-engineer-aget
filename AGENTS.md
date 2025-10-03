# Agent Configuration - AGET CLI Agent Template

@aget-version: 2.4.0

## 🚨 CRITICAL: INITIALIZATION PROCEDURE (REQUIRED)

**You MUST follow these steps IMMEDIATELY:**

**Step 1:** Check if file `AGENTS_AGET.md` exists in this directory
**Step 2:** If it exists, **READ IT IMMEDIATELY** for all AGET protocols
**Step 3:** Use the protocols from AGENTS_AGET.md for all standard commands
**Step 4:** Return here for AGET-specific development instructions

> ⚠️ **IMPORTANT**: This is the AGET framework repository itself. You are maintaining the tool that other agents use!

---

## Project Context

**AGET (Agent Template)** - The universal standard for making any codebase instantly CLI agent-ready. This is the reference implementation that all other projects use to become agent-compatible.

### Mission
Make CLI coding agents better collaborators through conversational command patterns and clean separation of framework vs project concerns.

### Current Version
- **v2.4.0 "Clarity"** (Naming conventions and organizational structure)
- **Released**: October 3, 2025
- **Coverage Target**: >80% for critical patterns

### v2.4.0 Features - Naming Conventions
- **Suffix Signaling**: `-AGET` (action-taking) vs `-aget` (information-only)
  - `my-github-AGET` = Can modify systems (write, commit, push)
  - `my-analytics-aget` = Read-only (analyze, report, recommend)
- **aget_group Field**: Organizational grouping for portfolio agents
- **managed_by Field**: Supervisor tracking for fleet coordination
- **Breaking Changes**: Naming convention required, aget_group for grouped agents

### v2.3.0 Features (Previous)
- Pattern Versioning, Session Metadata, Specification Framework
- Collaboration Tools, Intelligence Components

## AGET-Specific Development Commands

### Pattern Development
When user says "new pattern [category]/[name]":
1. Create `patterns/[category]/[name].py` with apply_pattern() function
2. Create `tests/test_[name].py` with comprehensive tests
3. Update `patterns/[category]/README.md` with documentation
4. Run tests to ensure >80% coverage

### Template Testing
When user says "test templates":
1. Run: `python3 -m pytest tests/test_installer.py -v`
2. Run: `python3 -m pytest tests/test_enhanced_installer.py -v`
3. Test each template type with --separate flag
4. Verify <60 second setup time

### Coverage Check
When user says "check coverage":
1. Run: `python3 -m pytest --cov=patterns --cov=aget --cov-report=term-missing`
2. Ensure overall coverage >80%
3. Critical patterns (wake, wind_down, sign_off) must be >85%
4. Report any gaps needing tests

## Testing Best Practices

### Directory Safety Pattern (CRITICAL)
Tests that manipulate directories MUST use defensive programming to prevent cascade failures:

```python
# SAFE setUp - Handles invalid cwd
def setUp(self):
    self.test_dir = Path(tempfile.mkdtemp())
    try:
        self.original_cwd = Path.cwd()
    except (FileNotFoundError, OSError):
        # Previous test left us in deleted directory
        import os
        os.chdir("/tmp")
        self.original_cwd = Path.cwd()

# SAFE tearDown - Handles errors gracefully
def tearDown(self):
    import os
    try:
        os.chdir(self.original_cwd)
    except (FileNotFoundError, OSError):
        os.chdir("/tmp")  # Fallback to safe location
    if self.test_dir.exists():
        shutil.rmtree(self.test_dir)
```

### Testing Guidelines
1. **Always wrap `Path.cwd()` in try/except** when tests change directories
2. **Prefer pytest fixtures** over manual setUp/tearDown when possible
3. **Use absolute paths** for file checks instead of relative paths
4. **Ensure tearDown handles partial failures** gracefully
5. **Never assume filesystem state** is stable between tests

### Release Validation
When user says "release check":
1. Run all tests: `python3 -m pytest tests/ -v`
2. Check coverage meets targets
3. Validate all templates work
4. Test on Mac and Linux
5. Verify backward compatibility
6. Check CHANGELOG.md is updated
7. Confirm version numbers consistent

### Pattern Validation
When user says "validate patterns":
1. Run: `python3 scripts/validate_patterns.py`
2. Ensure all patterns have apply_pattern() function
3. Check all patterns have tests
4. Verify pattern registry is complete

## Development Standards

### Code Quality Requirements
- **Test Coverage**: Minimum 80% overall, 85% for critical patterns
- **Performance**: All commands must complete in <2 seconds
- **Compatibility**: Must work on Python 3.8+
- **Dependencies**: Zero external dependencies (Python stdlib only)

### Dogfooding Requirements
1. **AGET uses its own patterns** - We eat our own dogfood
2. **Test on AGET first** - All changes tested here before release
3. **Evolution tracking** - Major decisions recorded in .aget/evolution/
4. **Include architecture** - This repo should use --separate mode

### Pattern Standards
Every pattern must:
1. Have an `apply_pattern()` function
2. Return a dictionary with status
3. Handle errors gracefully (no crashes)
4. Have >80% test coverage
5. Complete in <2 seconds

### Template Standards
Every template must:
1. Create valid AGENTS.md
2. Support --separate mode (v2.0+)
3. Create appropriate directories
4. Include README.md files
5. Work with --with-patterns flag

## Testing Workflows

### Before Committing (CI Check)
When user says "ci check", run these quick checks:
1. Check Python 3.8 compatibility: `python3 scripts/check_compatibility.py`
2. Run critical tests: `python3 -m pytest tests/test_critical_patterns.py -x -q`
3. Validate patterns: `python3 scripts/validate_patterns.py`

### Full Test Suite
1. Run: `python3 -m pytest tests/`
2. Check coverage: `python3 -m pytest --cov=. --cov-report=term-missing`
3. Test a fresh install: `python3 -m aget init /tmp/test-project --separate`

### Integration Testing
```bash
# Test all template types
for template in minimal standard agent tool hybrid; do
    python3 -m aget init /tmp/test-$template --template $template --separate
    python3 -m aget apply session/wake
done
```

## Release Process

### Version Bump
1. Update version in `aget/__init__.py`
2. Update version in templates/AGENTS_AGET.md
3. Update CHANGELOG.md with changes
4. Create evolution entry for release

### Pre-Release Checklist
- [ ] All tests passing
- [ ] Coverage >80%
- [ ] Templates tested with --separate
- [ ] Backward compatibility verified
- [ ] Documentation updated
- [ ] CHANGELOG.md current
- [ ] Evolution tracking complete

### Release Commands
```bash
# Tag release
git tag -a v2.0.0 -m "Release v2.0.0: Include Architecture"

# Push with tags
git push origin main --tags

# Create GitHub release
gh release create v2.0.0 --title "v2.0.0: Include Architecture" --notes-file CHANGELOG.md
```

## Important Files

### Core Framework
- `aget/` - Main AGET implementation
- `patterns/` - Reusable workflow patterns
- `templates/` - Agent configuration templates

### Critical Patterns
- `patterns/session/wake.py` - Session initialization (86% coverage target)
- `patterns/session/wind_down.py` - Work preservation (86% coverage target)
- `patterns/session/sign_off.py` - Quick save (80% coverage target)

### Templates
- `templates/AGENTS_AGET.md` - Master framework protocols
- `templates/AGENTS_v2.md` - Include architecture template

### Documentation
- `ROADMAP_v2.md` - Current development plan
- `docs/adr/` - Architecture decision records
- `.aget/evolution/` - Decision and discovery tracking

## Evolution Tracking

Record significant decisions and discoveries:
```bash
# Record a decision
python3 -m aget evolution --type decision "Implemented include architecture"

# Record a discovery
python3 -m aget evolution --type discovery "Procedural instructions work universally"

# View history
python3 -m aget evolution --list
```

## Troubleshooting AGET Development

### Pattern Not Loading
1. Check pattern has `apply_pattern()` function
2. Verify pattern is in correct directory structure
3. Check pattern registry includes it

### Template Issues
1. Verify template file exists in templates/
2. Check placeholder replacement logic
3. Test with --force flag

### Test Failures
1. Run specific test: `python3 -m pytest tests/test_name.py::test_function -v`
2. Check coverage gaps: `python3 -m pytest --cov=module --cov-report=html`
3. Review recent changes in git

---

## ✅ VERIFICATION CHECKLIST

Before any session, confirm you have:
- [ ] Read AGENTS_AGET.md for standard protocols
- [ ] Understood AGET-specific development requirements
- [ ] Checked current test coverage status
- [ ] Reviewed recent evolution entries
- [ ] Noted any failing tests or issues

**Remember**: You are maintaining the framework that makes all other projects agent-ready!

---

## Specification Creation (v2.2.0)

### When to Create Specs
User says: "create spec", "formal specification", "EARS spec", or "document capabilities formally"

### Specification Workflow

**Step 1: Read Format Documentation**
- File: `.aget/docs/SPEC_FORMAT_v1.1.md`
- Contains: EARS patterns, YAML structure, maturity levels, examples

**Step 2: Create Spec File**
- Location: `.aget/specs/{DOMAIN}_SPEC_v{VERSION}.yaml`
- Format: YAML with EARS temporal patterns
- Maturity levels:
  - **bootstrapping**: Simple capability list (no EARS)
  - **minimal**: EARS patterns with basic structure
  - **standard**: Full validation, test references
  - **exemplary**: Constitutional governance, comprehensive

**Step 3: Use Intelligence Tools**
- Run ambiguity detector on each capability
- During creation: Use detector logic to flag potential ambiguities
- Present flags to user for decision
- Add clarifications based on suggestions

### Intelligence Integration

**Ambiguity Detection (Automatic):**
- Proactively identify ambiguities during spec creation
- Use patterns from `.aget/intelligence/ambiguity_corpus.yaml`
- Present ambiguity flags with confidence scores
- User decides: accept flag, clarify, or reject
- Add clarifications to capability with `ambiguity_check` metadata

### EARS Pattern Quick Reference

1. **Ubiquitous**: The system shall [response]
2. **State-driven**: While [condition], the system shall [response]
3. **Event-driven**: When [trigger], the system shall [response]
4. **Optional**: Where [feature], the system shall [response]
5. **Unwanted**: If [condition], then the system shall [response]

---
*AGET v2.2.0 - Making CLI coding agents better collaborators*
*Intelligence-enabled specification creation with EARS patterns*