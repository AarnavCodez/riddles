import re


class Riddle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, guess):
        return self.answer.lower() == guess.lower()
