import sys
sys.path.insert(1, "./")

from server import server # noqa
from controllers import app # noqa

if __name__ == "__main__":
    server.run(app)
