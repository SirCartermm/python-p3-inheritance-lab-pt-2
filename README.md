Student Classes Test Suite
This repository contains a test suite for the Student and ChattyStudent classes.

Getting Started
Requirements
Python 3.7+
Pytest
Installation
Clone the repository: git clone https://github.com/your-username/student-classes-test-suite.git
Install Pytest: pip install pytest
Running the Tests
Navigate to the project directory: cd student-classes-test-suite
Run the tests: pytest
Tests
The test suite includes the following tests:

test_student.py: Tests for the Student class
test_hello: Tests the hello method
test_raise_hand: Tests the raise_hand method
test_chatty_student.py: Tests for the ChattyStudent class
test_hello: Tests the hello method
test_raise_hand: Tests the raise_hand method
Fixtures
The test suite uses fixtures to share setup and teardown code across multiple tests. The conftest.py file defines the following fixtures:

student: Returns an instance of the Student class
chatty_student: Returns an instance of the ChattyStudent class
captured_stdout: Captures the output of the hello and raise_hand methods
License
This project is licensed under the MIT License. See LICENSE for details.

Contributing
Contributions are welcome! If you'd like to contribute to the test suite, please open a pull request.

Author
[Sam Carter]