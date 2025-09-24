# Changelog

All notable changes to AGET will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0-alpha.2] - 2025-09-24

### Gate 2: Pattern Library Complete

#### Added
- **Pattern Library Foundation** with PatternRegistry for discovery and loading
- **8 Reusable Patterns**:
  - `session/wake` - Wake up protocol with git status and pattern detection
  - `session/wind_down` - Save work with commits, notes, and tests
  - `session/sign_off` - Quick save and exit without prompts
  - `housekeeping/cleanup` - Remove temp files, caches, build artifacts
  - `housekeeping/doc_check` - Assess documentation quality (A-F grades)
  - `bridge/extract_output` - Transform agent outputs to public products
  - `housekeeping/migration_cleanup` - Clean migration artifacts (existing)
  - `meta/project_scanner` - Scan projects for AGET readiness (existing)

#### Enhanced
- `aget init` now creates:
  - `outputs/` directory for agent workspace
  - `data/` directory for persistent storage
  - `.aget/evolution/` for tracking insights
  - Updated AGENTS.md template with vocabulary reference

- `aget apply` command:
  - Lists all available patterns
  - Applies patterns to projects
  - Provides helpful error messages
  - Performance <2 second requirement met

#### Testing
- Comprehensive test suites for all patterns
- 54 tests passing
- Test-first development approach
- Performance validation (<2s requirement)

## [2.0.0-alpha.1] - 2025-09-24

### Gate 1: Core CLI Foundation

#### Added
- `aget init` command with three-tier degradation (gh/git/filesystem)
- `aget rollback` command for safe configuration rollback
- Base command architecture for future expansion
- Test theater with quality agent architecture

#### Changed
- Unified v2 vision combining CLI tool with framework concepts
- Vocabulary distinction: outputs (private) vs Outputs (public)
- Naming convention: aget-* (framework), *-aget (agents)

## [1.0.0] - 2025-09-22

### Initial Release

#### Added
- Universal agent configuration via AGENTS.md
- Session management protocols (wake, wind down, sign off)
- Housekeeping protocols (cleanup, documentation check)
- Template installer with three tiers (minimal, standard, advanced)
- Support for multiple AI coding assistants
- Cross-platform compatibility (Mac, Linux, Windows)

---

*For detailed migration instructions from v1 to v2, see [UPGRADING.md](docs/UPGRADING.md)*