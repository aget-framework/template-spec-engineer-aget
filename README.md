# AGET: CLI Agent Template

> **Mission: Help CLI-using creators to build better software enjoyably faster (using CLI coding agents)**

**Agent Template (AGET)** - Cognitive augmentation framework for software and data work. Transform any project into a CLI agent-ready environment with conversational command patterns. Works with Claude Code, Cursor, Aider, Windsurf, and all major AI coding assistants.

**Current Version**: v2.3.0 "Collaboration"

## Branch Strategy
- **main branch**: Stable release (v2.3.0 "Collaboration")
- **develop branch**: Next features (v2.4.0+)
- See [.aget/BRANCHING.md](.aget/BRANCHING.md) for details

> **📍 Strategic Vision & Governance**: Vision and governance documents now live in [aget-aget](https://github.com/aget-framework/aget-aget). This repository focuses on stable implementation. See [GOVERNANCE_POINTER.md](docs/GOVERNANCE_POINTER.md) for details.

## Who This Is For

- **Software Owners** governing their project's evolution
- **Contributors** needing private workspace for external projects
- **Analysts** examining codebases without modifying
- **Data Scientists** organizing standalone analysis (Spotify, financial, etc.)
- **Developers** wanting consistent patterns across projects
- **Learners** using AI to understand and build software

## What This Provides

AGET implements a specification-driven development framework with:
- **Spec templates**: Define what you want before building
- **Session management**: `hey` → work → `wind down` → `sign off`
- **AI interaction**: Natural language commands that work consistently
- **Progressive understanding**: Start empty, grow knowledge over time
- **Universal compatibility**: Works with all major AI assistants

## Quick Start (30 Seconds)

### How AGET Works

AGET is not a traditional CLI tool. You interact through your AI assistant using natural language:

1. **Clone AGET** into your project:
```bash
git clone https://github.com/aget-framework/aget-cli-agent-template.git
cd aget-cli-agent-template
```

2. **Open with your AI coding assistant**:
```bash
# Claude Code (primary testing)
claude .

# Also works with: Cursor, Aider, Windsurf, Codex CLI, and other CLI agents
cursor . | aider . | windsurf .
```

3. **Start with natural language**:
```
You: hey
AI: [Checks environment, reports status, ready for commands]

You: initialize this as an agent project
AI: [Sets up agent structure with workspace/, products/, docs/]

You: create a Python scraper tool
AI: [Builds tool in workspace/, adds tests, documentation]
```

### Behind the Scenes

Your AI assistant discovers and uses AGET patterns automatically. You never type `aget` commands directly - the AI handles that based on your natural language requests.

For more installation options and customization, see [docs/GET_STARTED.md](docs/GET_STARTED.md)

## 🚀 Try It Now! (2 Minutes)

Experience AGET with your AI assistant immediately:

```bash
# 1. Clone and enter the template
git clone https://github.com/aget-framework/aget-cli-agent-template.git
cd aget-cli-agent-template

# 2. Open with your AI assistant (Claude, Cursor, etc.)
claude .  # or: cursor . | code . | aider

# 3. Tell your AI assistant:
"hey"
```

Your AI will respond with project status, available patterns, and be ready for natural language commands like:
- `"run tests"` - Execute test suite
- `"check documentation"` - Analyze docs quality
- `"tidy up"` - Clean temporary files
- `"wind down"` - Save session and commit

### Live Example Session

```
You: hey

AI: Good morning! Let me check your environment...
    ✓ Working directory: ~/aget-cli-agent-template
    ✓ Git status: On branch main, clean
    ✓ Python version: 3.11.5
    ✓ Available patterns: 15 installed
    Ready for your commands!

You: let's build a Python web scraper tool

AI: I'll help you create a web scraper. Let me start by creating the project structure...
    [Creates workspace/scraper.py with requests and BeautifulSoup]
    ✓ Created main scraper module
    ✓ Added error handling and rate limiting
    ✓ Included user-agent headers
    Shall I add tests?

You: yes, and make it installable

AI: Creating package structure...
    [Creates setup.py, requirements.txt, tests/]
    ✓ Package structure created
    ✓ Unit tests added (3 passing)
    ✓ Installation tested successfully
    You can now: pip install -e .

You: wind down

AI: Saving session...
    ✓ Created session notes: SESSION_NOTES/2025-09-28.md
    ✓ Committed changes: "feat: Add hello world example"
    Session duration: 2 minutes
    Have a great day!
```

## Installation

> **⚠️ Important**: AGET is not a traditional CLI tool. You don't run `aget` commands directly. Instead, your AI assistant uses AGET patterns based on your natural language requests.

### Prerequisites
- Python 3.8 or higher
- Git
- Basic command-line familiarity

### Method 1: Clone and Use Directly (Recommended)
```bash
# Clone the template repository
git clone https://github.com/aget-framework/aget-cli-agent-template.git

# Navigate to your project directory
cd ~/your-project

# Run aget commands using Python module syntax
python3 /path/to/aget-cli-agent-template/aget/__main__.py init
```

### Method 2: Create Alias for Convenience
Add to your shell configuration file (`~/.bashrc`, `~/.zshrc`, etc.):
```bash
alias aget="python3 /path/to/aget-cli-agent-template/aget/__main__.py"
```

Then reload your shell:
```bash
source ~/.bashrc  # or ~/.zshrc
```

Now you can use:
```bash
aget init
aget validate
aget list
```

## Usage

> **Note**: The commands below are what your AI assistant can execute behind the scenes. You interact through natural language like "hey", "initialize this", "run tests", not by typing these commands.

### Core Commands (AI Executes These)

#### Initialize a New Agent
```bash
# Create agent with standard patterns (recommended)
aget init --template agent --with-patterns

# Create tool with minimal patterns
aget init --template tool --with-patterns minimal

# Create hybrid agent/tool
aget init --template hybrid --with-patterns advanced
```

#### Validate Your Setup
```bash
# Check if your project meets AGET standards
aget validate

# Detailed validation with recommendations
aget validate --verbose
```

#### List Available Patterns
```bash
# Show all available patterns
aget list

# Show installed patterns
aget list --installed

# Show patterns by category
aget list --category session
```

#### Extract Tools to Products
```bash
# Extract a tool from workspace to products
aget extract --from workspace/my_tool.py --to products/

# Extract with dependencies
aget extract --from workspace/analyzer.py --to products/ --with-deps
```

### Session Management Commands
Your AI assistant will understand these natural language commands:

- **`hey`** or **`wake up`** - Start a session, check status
- **`wind down`** or **`save work`** - Save session with detailed notes
- **`sign off`** or **`all done`** - Quick save and exit
- **`tidy up`** - Clean temporary files
- **`deep clean`** - Archive old files and reorganize
- **`health check`** - Run diagnostics when something's wrong

### Working with Patterns
```bash
# Install a specific pattern
python3 patterns/session/session_manager.py --install

# Run a pattern directly
python3 patterns/housekeeping/cleanup.py --dry-run

# Check pattern documentation
python3 patterns/documentation/check_docs.py --help
```

## Why Universal Standards?

### The Configuration Fragmentation Problem

The current landscape of AI coding assistants creates configuration overhead. Each tool requires its own format:

- **Claude Code**: Reads `CLAUDE.md` for agent-specific instructions
- **Cursor**: Requires `.cursorrules` for behavior configuration
- **Windsurf**: Uses `.windsurfrules` for custom patterns
- **Aider**: Expects `.aider.conf.yml` for settings
- **GitHub Copilot**: Uses `.github/copilot-instructions.md`

This fragmentation means maintaining multiple configuration files with duplicated content. Using multiple tools requires synchronizing changes across 3-5 different formats.

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

## What's New in v2 (Enhanced with Real Migration Experience!)

### 🚀 Working CLI Commands
- `aget init --template [agent|tool|hybrid] --with-patterns` - One-step complete setup ✅ **ENHANCED!**
- `aget apply <pattern>` - Apply reusable patterns to your project ✅
- `aget list` - Discover available patterns ✅
- `aget rollback` - Safe rollback mechanism for configurations ✅
- `aget extract --from src/ --to products/` - Extract entire directories ✅ **ENHANCED!**
- `aget evolution --type [decision|discovery]` - Track your agent's evolution ✅

### 🎯 Major Enhancements (Based on Real Migrations)
- **One-Command Setup**: `--with-patterns` flag eliminates confusing two-step process
- **Directory Extraction**: Extract entire `src/` directories, not just single files
- **Structure Preservation**: Maintains directory hierarchy when extracting
- **94% Time Reduction**: Complete setup in <1 minute vs 15+ minutes
- **Smart Pattern Mapping**: Each template automatically applies appropriate patterns

### 📦 Template Scaffolding
- **agent**: Full autonomous agent structure with workspace/products split
- **tool**: Traditional tool/library structure
- **hybrid**: Combined agent and tool capabilities
- **minimal**: Basic configuration only
- **standard**: Default balanced template

### 🌉 Enhanced Bridge Mechanism
- Extract entire directories: `aget extract --from src/ --to products/`
- Maintains package structure with proper `__init__.py` files
- Automatic secret sanitization and API key removal
- Generated setup.py and README for pip installation
- Track extractions in evolution history

### 📈 Evolution Tracking (Gate 3 Feature)
- Record decisions: `aget evolution --type decision "Why we chose X"`
- Capture discoveries: `aget evolution --type discovery "Found pattern Y"`
- Track extractions: Automatic when using `aget extract`
- View history: `aget evolution --list`

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
       ✓ Working directory: ~/project
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

- [Getting Started](docs/GET_STARTED.md) - Get running in 30 seconds
- [Understanding Patterns](docs/EXPLORE_FEATURES.md) - Learn how patterns work
- [Why AGET](docs/UNDERSTAND_AGET.md) - The value proposition
- [Troubleshooting](docs/FIX_PROBLEMS.md) - Common issues and solutions
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

## Mission

Help CLI developers build better software faster with AI assistance. [Details](docs/MISSION.md).