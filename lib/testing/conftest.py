# conftest.py

import pytest

@pytest.fixture
def student():
    return Student()

