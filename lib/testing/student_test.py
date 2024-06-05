import unittest
from unittest.mock import patch
from io import StringIO
from student import Student, ChattyStudent

class TestStudent(inittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_Student_hello(self, mock_stdout):
        student = Student()
        student.hello()
        self.assertEqual(mock_stdout.getvalue().strip(), "Hey ther! I'm so excited to learn stuff.")

    @patch('sys.stdout', new_callable=StringIO)
    def test_student_raise_hand(self, mock_stdout):
        student = Student()
        student.raise_hand()
        self.assertEqual(mock_stdout.getvalue().strip(), "Pick me!")

class TestChattyStudent(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_chatty_student_hello(Self, mock_stdout):
        chatty_student = ChattyStudent()
        chatty_student.hello()
        