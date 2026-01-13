"""Pytest configuration file."""
import sys
from pathlib import Path

# Add the root directory to the Python path so tests can import main
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))
