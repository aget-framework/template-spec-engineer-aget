"""
Config Module - All v2.0 functionality lives here.
In v2.1+ this becomes 'aget config' subcommand.
"""

from typing import List


class ConfigModule:
    """Handles all configuration-related commands."""

    def __init__(self):
        """Initialize config module with command registry."""
        self.commands = {
            'init': self.cmd_init,
            'validate': self.cmd_validate,
            'apply': self.cmd_apply,
            'rollback': self.cmd_rollback,
            'list': self.cmd_list,
        }

    def handle(self, command: str, args: List[str]) -> int:
        """Handle a config subcommand."""
        if command not in self.commands:
            print(f"Error: Unknown config command '{command}'")
            return self.show_help()

        return self.commands[command](args)

    def show_help(self) -> int:
        """Show config module help."""
        print("""
Config Module Commands:
  init        Initialize agent configuration
  validate    Validate AGENTS.md syntax
  apply       Apply a pattern to configuration
  rollback    Restore previous configuration
  list        List available patterns
""")
        return 0

    def cmd_init(self, args: List[str]) -> int:
        """Initialize command - will use InitCommand class."""
        # Placeholder for Step 3
        from aget.config.commands.init import InitCommand
        cmd = InitCommand()
        result = cmd.execute(args=args)
        if result['success']:
            print(f"✅ Configuration initialized ({result['tier_used']} tier)")
            if result['execution_time'] < 2.0:
                print(f"⚡ Completed in {result['execution_time']:.2f}s")
            return 0
        else:
            print(f"❌ Error: {result.get('error', 'Unknown error')}")
            return 1

    def cmd_validate(self, args: List[str]) -> int:
        """Validate command - placeholder."""
        print("Validate command - coming in Step 3")
        return 0

    def cmd_apply(self, args: List[str]) -> int:
        """Apply command - placeholder."""
        print("Apply command - coming in Phase 2")
        return 0

    def cmd_rollback(self, args: List[str]) -> int:
        """Rollback command - restore previous configuration."""
        from aget.config.commands.rollback import RollbackCommand
        cmd = RollbackCommand()
        result = cmd.execute(args=args)

        if result.get('action') == 'list':
            # List mode
            backups = result.get('backups', [])
            if backups:
                print("Available backups:")
                for backup in backups[:5]:  # Show recent 5
                    print(f"  {backup['id']} - {backup['reason']}")
            else:
                print("No backups available")
            return 0
        elif result['success']:
            print(f"✅ Rollback successful ({result['tier_used']} tier)")
            print(f"   Restored: {result['files_restored']} files")
            if result['execution_time'] < 2.0:
                print(f"⚡ Completed in {result['execution_time']:.2f}s")
            return 0
        else:
            print(f"❌ Error: {result.get('error', 'Unknown error')}")
            return 1

    def cmd_list(self, args: List[str]) -> int:
        """List command - placeholder."""
        print("List command - coming in Phase 2")
        return 0