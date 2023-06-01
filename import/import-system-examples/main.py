# Runs the tests that cover topics from the official documentation:
# https://docs.python.org/3/reference/import.html

import pytest
import os

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    retcode = pytest.main(["-x", os.path.join(base_dir, "test")])
