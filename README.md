# AGET: CLI Agent Template

**Agent Template (AGET)** - The universal standard for making any codebase instantly CLI agent-ready. Works with Claude Code, Cursor, Aider, Windsurf, and all major AI coding assistants.

A reference implementation of the [CLI Agent Template Framework](https://www.aget-framework.com/RKB/CLI_Agent_Template_Framework) - transform any codebase into a CLI coding agent-ready collaborative environment through conversational command patterns.

## Who This Is For

- **Developers** using AI coding assistants (Claude Code, Cursor, Aider, Windsurf)
- **Teams** wanting consistent AI workflows across projects
- **Open source maintainers** making projects more contributor-friendly
- **Solo developers** tired of repeating setup instructions to AI

## What This Provides

AGET implements a [workflow automation framework](https://www.aget-framework.com/RKB/CLI_Agent_Template_Framework) with:
- **Session management**: `hey` → work → `wind down` → `sign off`
- **Universal compatibility**: One config works for ALL AI agents
- **Self-documenting patterns**: AI agents understand your workflow instantly
- **Zero lock-in**: Just Python scripts, no proprietary tools

## Quick Start (30 Seconds)

```bash
# Clone and install AGET in your project
git clone https://github.com/aget-framework/aget-cli-agent-template.git
cd aget-cli-agent-template
python3 installer/install.py /path/to/your/project

# Or use the new aget commands (v2 Alpha):
aget init                    # Initialize agent configuration
aget apply session/wake      # Apply session patterns
aget apply housekeeping/cleanup  # Apply cleanup patterns

# Tell your AI: "hey"
# AI responds with project status and is ready to work

# That's it! Your project is now AI-agent ready
```

For more installation options and customization, see [docs/QUICK_START.md](docs/QUICK_START.md)

## Why Universal Standards?

### The Configuration Fragmentation Problem

The current landscape of AI coding assistants has created a significant maintenance burden for development teams. Each tool requires its own configuration format:

- **Claude Code**: Reads `CLAUDE.md` for agent-specific instructions
- **Cursor**: Requires `.cursorrules` for behavior configuration
- **Windsurf**: Uses `.windsurfrules` for custom patterns
- **Aider**: Expects `.aider.conf.yml` for settings
- **GitHub Copilot**: Uses `.github/copilot-instructions.md`

This fragmentation forces teams to maintain multiple configuration files with largely duplicated content. A typical multi-tool setup requires developers to synchronize changes across 3-5 different configuration formats, increasing the risk of inconsistencies and configuration drift.

## What You Get

After installation, your CLI agent can understand commands like:

- **`hey`** - Initialize session with project status
- **`tidy up`** - Clean temporary files and caches
- **`deep clean`** - Deep cleanup with archiving
- **`check docs`** - Analyze documentation quality
- **`health check`** - Emergency diagnostics when something's wrong
- **`save work`** - Save session state and commit changes
- **`all done`** - Quick commit and push

## Features

✅ **Natural Language Commands** - Conversational interface for common tasks
✅ **Progressive Safety** - Dry-run → Modify → Reorganize
✅ **Session Management** - Context preservation across conversations
✅ **Emergency Recovery** - Diagnostic and recovery protocols
✅ **Documentation as Code** - Quality checks and auto-fixes
✅ **Git Integration** - Smart commits, checkpoints, and rollbacks

## Templates

### Minimal (5 patterns)
Basic setup with session management only. Perfect for small projects.

```bash
# After repository goes public:
curl -sSL https://raw.githubusercontent.com/aget-framework/aget-cli-agent-template/main/install.sh | bash -s . minimal

# For now, use git clone method:
git clone https://github.com/aget-framework/aget-cli-agent-template.git
cd aget-cli-agent-template
python3 installer/install.py /path/to/your/project --template minimal
```

### Standard (15+ patterns) - Recommended
Full conversational interface with housekeeping and documentation checks.

```bash
# After repository goes public:
curl -sSL https://raw.githubusercontent.com/aget-framework/aget-cli-agent-template/main/install.sh | bash

# For now, use git clone method:
git clone https://github.com/aget-framework/aget-cli-agent-template.git
cd aget-cli-agent-template
python3 installer/install.py /path/to/your/project --template standard
```

### Advanced (25+ patterns)
Everything including CI/CD integration, advanced testing, and compliance checks.

```bash
# After repository goes public:
curl -sSL https://raw.githubusercontent.com/aget-framework/aget-cli-agent-template/main/install.sh | bash -s . advanced

# For now, use git clone method:
git clone https://github.com/aget-framework/aget-cli-agent-template.git
cd aget-cli-agent-template
python3 installer/install.py /path/to/your/project --template advanced
```

## What's New in v2 (Beta Ready - Gate 2 Complete)

### 🚀 Working CLI Commands
- `aget init` - Initialize agent configuration with directory structure ✅
- `aget apply <pattern>` - Apply reusable patterns to your project ✅
- `aget list` - Discover available patterns ✅
- `aget rollback` - Safe rollback mechanism for configurations ✅

### 📦 Pattern Library (8 patterns functional)
- **Session Patterns**: wake, wind_down, sign_off - Start and manage agent sessions
- **Housekeeping**: cleanup, doc_check, migration_cleanup - Maintain project health
- **Bridge Pattern**: extract_output - Transform private outputs→public Outputs
- **Meta**: project_scanner - Multi-project management

### 🌉 Framework Vision
- Transform agent outputs into public products
- Bridge private exploration to community value
- Evolution tracking in `.aget/evolution/`

## Supported CLI Agents

- [Claude Code](https://claude.ai/code) (Primary target)
- [Cursor](https://cursor.sh)
- [Aider](https://aider.chat)
- [Windsurf](https://codeium.com/windsurf)
- [Mentat](https://github.com/AbanteAI/mentat)
- Any CLI-based AI coding assistant

## Project Structure

```
your-project/
├── AGENTS.md                 # Universal agent configuration (AGENTS.md specification)
├── CLAUDE.md                 # Symlink to AGENT.md (backward compatibility)
├── scripts/
│   ├── session_protocol.py   # Wake up, wind down, sign off
│   ├── housekeeping_protocol.py  # Cleaning and organization
│   └── recovery_protocol.py  # Emergency diagnostics
├── patterns/                 # Reusable workflow patterns
│   ├── session/             # Session management patterns
│   ├── housekeeping/        # Maintenance patterns
│   └── documentation/       # Documentation patterns
└── .session_state.json      # Session persistence
```

## How It Works

1. **Agent reads AGENTS.md** - Discovers available conversational command patterns
2. **Pattern discovery** - Agent automatically identifies workflow patterns from configuration
3. **Natural language triggers** - You say "hey", agent executes the corresponding pattern
4. **Safe-by-default** - Dry-run previews, rollback support, confirmation prompts
5. **Session persistence** - Context preservation across agent restarts

## Examples

### Starting a Session
```
You: hey
Agent: Running wake protocol...
       ✓ Working directory: /Users/you/project
       ✓ Git status: 3 uncommitted changes
       ✓ Tests: 47 passing
       ✓ Documentation: Grade B
       Ready for tasks.
```

### Cleaning Up
```
You: spring clean
Agent: Running spring clean protocol (dry-run)...
       Would archive 5 old session notes
       Would remove 127 __pycache__ files
       Would clean 3.2MB temp files
       Run without --dry-run to execute.
```

### Emergency Recovery
```
You: sanity check
Agent: Running emergency diagnostics...
       ✓ Python 3.11.0
       ✓ Git repository OK
       ✓ Critical files present
       ✓ Imports working
       System Status: OK
```

## Documentation

- [Quick Start Guide](docs/QUICK_START.md) - Get running in 30 seconds
- [Understanding Patterns](docs/PATTERNS_EXPLAINED.md) - Learn how patterns work
- [Why This Matters](docs/WHY_THIS_MATTERS.md) - The value proposition
- [Troubleshooting](docs/TROUBLESHOOTING.md) - Common issues and solutions
- [Framework Concept](https://www.aget-framework.com/RKB/CLI_Agent_Template_Framework) - Academic reference

## Upgrading

Already using the template? See [UPGRADING.md](UPGRADING.md) for how to apply template enhancements to your existing projects. The guide provides a five-phased approach that preserves your customizations while getting new features.

## Contributing

This repository implements [dogfooding practices](https://www.aget-framework.com/RKB/CLI_Agent_Template_Framework) - it uses its own patterns for self-maintenance. To contribute:

1. Fork and clone
2. Say "hey" to your CLI agent
3. Make changes following existing patterns
4. Say "test templates" to run tests
5. Say "wind down" to save your session
6. Submit a pull request

## Pattern Development

To add a new pattern:

1. Create in `patterns/<category>/<pattern_name>.py`
2. Add tests in `tests/test_<pattern_name>.py`
3. Document in `patterns/<category>/README.md`
4. Update the installer to include it

## Versioning

This project uses semantic versioning. Each pattern has its own version number, allowing selective updates.

## License

MIT - See [LICENSE](LICENSE) file

## Acknowledgments

Patterns evolved from real-world usage in production codebases, especially the RKB content enhancement project.

---

*Making CLI coding agents better collaborators, one pattern at a time.*