# CLI Agent Template - Universal Agent Configuration

## Agent Compatibility
This configuration works with Claude Code, Cursor, Aider, Windsurf, and other CLI coding agents.
**Note**: CLAUDE.md is a symlink to this file for backward compatibility.

## Project Context
This repository provides templates and patterns for making codebases CLI agent-ready.
**Important**: This repository dogfoods its own patterns - all commands defined here work in this repo!

## Session Management Protocols

### Start Session (Wake Up Protocol)
When user says "hey" or "wake up", immediately execute:
- Read AGENTS.md (to memorize all trigger phrases and configurations)
- Run: `python3 scripts/aget_session_protocol.py wake`
- This will show working directory, pattern status, and git status
- Reports findings using "## Status Report" header
- Ends with "Ready for tasks."

### Save Work (Wind Down Protocol)
When user says "save work" or "wind down", execute:
- Run: `python3 scripts/aget_session_protocol.py wind-down`
- This will commit changes, create session notes, run tests
- Reports "Session preserved."

### End Session (Sign Off Protocol)
When user says "all done", "sync up", or "sign off", execute:
- Run: `python3 scripts/aget_session_protocol.py sign-off`
- This will quick commit and push changes
- Reports "Signed off."

## Housekeeping Protocols

### Documentation Check
When user says "check docs" or "documentation check", execute:
- Run: `python3 scripts/aget_housekeeping_protocol.py documentation-check`
- Analyzes documentation quality
- Reports grade (A-F) and issues found

### Light Cleanup (Housekeeping)
When user says "tidy up" or "housekeeping", execute:
- Run: `python3 scripts/aget_housekeeping_protocol.py housekeeping`
- Cleans temp files, caches, Python artifacts
- Always run with --dry-run first

### Deep Clean
When user says "deep clean" or "spring clean", execute:
- Run: `python3 scripts/aget_housekeeping_protocol.py spring-clean --dry-run`
- Archives old files, removes duplicates, cleans empty dirs
- Requires confirmation if not dry-run

### Health Check (System Diagnostic)
When user says "health check" or "sanity check", execute:
- Run: `python3 scripts/aget_housekeeping_protocol.py sanity-check`
- Checks Python, git, critical files, imports
- Reports system status: OK/DEGRADED/CRITICAL

## Template Management Commands

### Check Template Status
When user says "status" or "template status", execute:
- Run: `python3 installer/status.py`
- Shows installed patterns and versions
- Lists available updates

### Update Templates
When user says "update templates", execute:
- Run: `python3 installer/update.py --check`
- Shows which patterns have updates available
- User can then update specific patterns

### Test Templates
When user says "test templates", execute:
- Run: `python3 -m pytest tests/ -v`
- Runs all template tests
- Validates patterns work correctly

## Development Workflow

### Pattern Development
When working on new patterns:
1. Create in `patterns/<category>/<pattern_name>.py`
2. Add tests in `tests/test_<pattern_name>.py`
3. Document in `patterns/<category>/README.md`
4. Update VERSION file

### Testing Changes
Before committing:
- Run: `python3 -m pytest tests/`
- Run: `python3 scripts/validate_patterns.py`

## Important Notes
- This repository uses its own patterns (dogfooding)
- All patterns must work both standalone and integrated
- Maintain backwards compatibility when updating patterns
- Document all breaking changes in CHANGELOG.md