class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")


class ChattyStudent(Student):
    def hello(self):
        super().hello()
        print("How are you doing today? I'm so excited to learn stuff.")
        print("Oh, by the way, did you see the latest episode of my favorite show?")
        print("I can't believe who died...")  # Ensure exactly three dots

    def raise_hand(self):
        for _ in range(10):
            print("Pick me!")
           


