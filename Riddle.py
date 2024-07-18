import re


class Riddle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, guess):
        a = re.compile(rf"{self.answer}")
        return a.search(guess)
