import unittest
from unittest.mock import patch
from io import StringIO
from student import Student, ChattyStudent

class TestStudent(unittest.TestCase):
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
        Self.assertEqual(mock_stdout.getvalue().strip(), "Hey ther! I'm so excited to learn stuff.")


class TestChattyStudent(unittest.TestCase):
     @patch('sys.stdout', new_callable=StringIO)
       def test_chatty_student_hello(self, mock_stdout):
         chatty_student = ChattyStudent()
         chatty_student.hello()
         expected_output = """Hey there! I'm so excited to learn stuff.
  How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? okay well let mejust tell you who died ..."""
          self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
     def test_chatty_student_raise_hand(self, mock_stdout):
    chatty_student = ChattyStudent()
    chatty_student.raise_hand()
    expected_output = "Pick me!\n" * 10
    Self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()