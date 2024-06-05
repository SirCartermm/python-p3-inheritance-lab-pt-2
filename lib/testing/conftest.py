# conftest.py

from unittest.mock import patch
import pytest

from lib.student import ChattyStudent, Student

@pytest.fixture
def student():
    return Student()

@pytest.fixture
def chatty_student():
    return ChattyStudent()

@pytest.fixture
def captured_stdout():
    with patch('sys.stdout' new_callable=StringIO) as mock_stdout:
          yield mock_stdout



