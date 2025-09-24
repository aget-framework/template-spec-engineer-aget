#!/usr/bin/env python3
"""Test session patterns."""

import sys
import json
import tempfile
from pathlib import Path
from datetime import datetime, timedelta
import time

sys.path.insert(0, '.')
from patterns.session.wake import WakeProtocol


def create_test_project(tmpdir: Path):
    """Create a test project structure."""
    tmpdir.mkdir(exist_ok=True)

    # Create AGENTS.md
    agents_file = tmpdir / "AGENTS.md"
    agents_file.write_text("""# Agent Configuration
## Session Protocols
Wake up protocol configured.
""")

    # Create git repo
    import subprocess
    subprocess.run(['git', 'init'], cwd=tmpdir, capture_output=True)
    subprocess.run(['git', 'config', 'user.email', 'test@example.com'], cwd=tmpdir, capture_output=True)
    subprocess.run(['git', 'config', 'user.name', 'Test User'], cwd=tmpdir, capture_output=True)
    subprocess.run(['git', 'add', '.'], cwd=tmpdir, capture_output=True)
    subprocess.run(['git', 'commit', '-m', 'Initial'], cwd=tmpdir, capture_output=True)

    # Create patterns
    (tmpdir / "patterns" / "session").mkdir(parents=True)
    (tmpdir / "patterns" / "housekeeping").mkdir(parents=True)

    # Create tests
    (tmpdir / "tests").mkdir()
    (tmpdir / "tests" / "test_example.py").write_text("# Test file")

    # Commit everything to git
    subprocess.run(['git', 'add', '.'], cwd=tmpdir, capture_output=True)
    subprocess.run(['git', 'commit', '-m', 'Add tests'], cwd=tmpdir, capture_output=True)

    return tmpdir


def test_wake_protocol_first_session():
    """Test wake protocol on first session."""
    print("Testing wake protocol - first session...")
    print("-" * 40)

    with tempfile.TemporaryDirectory() as tmpdir:
        project = create_test_project(Path(tmpdir))

        # Execute wake protocol
        protocol = WakeProtocol(project)
        result = protocol.execute()

        # Check result structure
        assert 'timestamp' in result
        assert 'status' in result
        assert result['status'] == 'ready'
        assert result['session_number'] == 1
        assert result['last_session'] == 'First session'

        # Check git status was checked
        assert 'git' in result['checks']
        assert result['checks']['git']['is_repo'] == True
        assert result['checks']['git']['clean'] == True

        # Check patterns were found
        assert 'patterns' in result['checks']
        assert 'session' in result['checks']['patterns']
        assert 'housekeeping' in result['checks']['patterns']

        # Check tests were counted (we created test_example.py)
        assert 'tests' in result['checks']
        assert result['checks']['tests'] >= 1  # At least one test file

        print("✅ First session wake protocol works")


def test_wake_protocol_subsequent_session():
    """Test wake protocol on subsequent sessions."""
    print("\nTesting wake protocol - subsequent session...")
    print("-" * 40)

    with tempfile.TemporaryDirectory() as tmpdir:
        project = create_test_project(Path(tmpdir))

        # First session
        protocol = WakeProtocol(project)
        result1 = protocol.execute()
        assert result1['session_number'] == 1

        # Wait a moment
        time.sleep(0.1)

        # Second session
        result2 = protocol.execute()
        assert result2['session_number'] == 2
        assert result2['last_session'] != 'First session'
        assert 'Just now' in result2['last_session'] or 'seconds' in result2['last_session']

        print(f"✅ Session tracking works (session #{result2['session_number']})")
        print(f"✅ Time tracking works ({result2['last_session']})")


def test_session_state_persistence():
    """Test that session state persists."""
    print("\nTesting session state persistence...")
    print("-" * 40)

    with tempfile.TemporaryDirectory() as tmpdir:
        project = create_test_project(Path(tmpdir))

        # Create first protocol instance
        protocol1 = WakeProtocol(project)
        result1 = protocol1.execute()

        # Check state file was created
        state_file = project / ".session_state.json"
        assert state_file.exists(), "State file should be created"

        # Load state directly
        state = json.loads(state_file.read_text())
        assert state['session_count'] == 1
        assert state['last_wake'] is not None
        assert 'current_session' in state

        # Create new protocol instance (simulating new agent session)
        protocol2 = WakeProtocol(project)
        result2 = protocol2.execute()

        # Check state was updated
        state = json.loads(state_file.read_text())
        assert state['session_count'] == 2

        print("✅ Session state persists correctly")


def test_git_dirty_detection():
    """Test detection of uncommitted changes."""
    print("\nTesting git dirty detection...")
    print("-" * 40)

    with tempfile.TemporaryDirectory() as tmpdir:
        project = create_test_project(Path(tmpdir))

        # Create uncommitted change
        (project / "new_file.txt").write_text("uncommitted")

        protocol = WakeProtocol(project)
        result = protocol.execute()

        assert result['checks']['git']['clean'] == False
        assert len(result['checks']['git']['changes']) > 0

        print("✅ Detects uncommitted git changes")


def test_wake_protocol_performance():
    """Test that wake protocol completes quickly."""
    print("\nTesting wake protocol performance...")
    print("-" * 40)

    with tempfile.TemporaryDirectory() as tmpdir:
        project = create_test_project(Path(tmpdir))

        protocol = WakeProtocol(project)

        start = time.time()
        result = protocol.execute()
        duration = time.time() - start

        assert duration < 2.0, f"Wake protocol took {duration:.2f}s (should be <2s)"
        print(f"✅ Performance: {duration:.3f}s (requirement: <2s)")


if __name__ == "__main__":
    print("🌅 Session Pattern Tests")
    print("=" * 40)

    test_wake_protocol_first_session()
    test_wake_protocol_subsequent_session()
    test_session_state_persistence()
    test_git_dirty_detection()
    test_wake_protocol_performance()

    print("\n" + "=" * 40)
    print("✅ ALL SESSION PATTERN TESTS PASSED")