"""Runs the configured application"""

import sys
sys.path.insert(1, "./")  # Sets 'src' directory as sources root

from server import server  # noqa: E402
from controllers import app  # noqa: E402

if __name__ == "__main__":
    server.run(app)
