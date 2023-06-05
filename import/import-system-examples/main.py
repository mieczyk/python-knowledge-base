# Runs the tests that cover topics from the official documentation:
# https://docs.python.org/3/reference/import.html

import pytest
from pathlib import Path

if __name__ == "__main__":
    base_dir = Path(__file__).parent.absolute()
    retcode = pytest.main(["-x", base_dir / "test"])
