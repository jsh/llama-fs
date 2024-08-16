"""
Is current Python version at least minimum required version?
"""

from packaging.version import Version
import sys

if __name__ == "__main__":
  # take minimum required version from cmdline
  if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <minimum_version>")
    sys.exit(1)
  minimum_version = Version(sys.argv[1])
  current_version = Version(sys.version.split()[0])
  if current_version < minimum_version:
    sys.exit(f"Python version ({current_version}) must be >= {minimum_version}")
