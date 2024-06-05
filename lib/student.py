3 #student.py


class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

class Student:
    # ... (hello method remains the same)
    def raise_hand(self):
        print("Pick me!")

class ChattyStudent(Student):
    def hello(self):
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Diid you watch The Walking Dead last night? You didn't?! oh man, it was so crazy! what, you don't want any spoilers? Okay well let me just tell you who died...")


      def raise_hand(self):
          for _ in range(10):
              super().raise_hand()

