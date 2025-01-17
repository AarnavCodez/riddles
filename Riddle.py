import random

def extract_equation(operand1, operator, operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2
    elif operator == "**":
        return operand1 ** operand2
    elif operator == "%":
        return operand1 % operand2
    else:
        return None

class Riddle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def get_question(self):
        """Return the riddle question."""
        return self.question

    def check_answer(self, guess):
        """Check the user's answer for the riddle."""
        return guess.strip().lower() == self.answer.strip().lower()

class Math:
    def __init__(self, expression, solution):
        self.expression = expression
        self.solution = solution

    def get_question(self):
        """Return the math expression as a question."""
        return self.expression

    def check_answer(self, guess):
        """Check if the user's answer is within a tolerance of 0.01."""
        try:
            return abs(float(guess) - self.solution) <= 0.01
        except ValueError:
            return False

    @staticmethod
    def generate_problems(range_min, range_max, amount):
        problems = []
        for _ in range(amount):
            operand1 = random.randint(range_min, range_max)
            operand2 = random.randint(range_min, range_max)
            operator = random.choice(['+', '-', '*', '/'])
            expression = f"{operand1} {operator} {operand2}"
            solution = extract_equation(operand1, operator, operand2)
            problems.append(Math(expression, solution))
        return problems
