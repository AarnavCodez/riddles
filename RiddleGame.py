import random
import Riddle

correct_feedback = ['Nice, You got it!', 'Your doing great!', 'Correct answer!', "Wow, you're smart!",
                    'You\'re on the run!']
incorrect_feedback = ['Nice try, but that\'s not it', 'Incorrect answer', 'You can try again later',
                      'Sorry, that isn\'t right']


class RiddleGame:
    def __init__(self, riddle_file):
        self.riddles = self.load_riddles(riddle_file)
        self.score = 0
        self.results = []
        self.question = 0
        self.answer = ""

    def load_riddles(self, riddle_file):

        riddles = []
        with open(riddle_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if ':' in line:
                    self.question, self.answer = line.split(':')
                    riddles.append(Riddle.Riddle(self.question.strip(), str(self.answer.strip())))

        return riddles



    def play(self):
        print("Welcome to the Riddle Game!")
        for riddle in self.riddles:
            print("\nRiddle/Math:")
            print(riddle.question)
            guess = input("Your answer: ").strip()
            if riddle.check_answer(guess):
                print(random.choice(correct_feedback))
                self.score += 1
                self.results.append((riddle.question, guess, True))
            else:
                print(f"{random.choice(incorrect_feedback)}. The correct answer was: {riddle.answer}")
                self.results.append((riddle.question, guess, False))

        self.show_summary()

    def show_summary(self):
        print("\nGame Over!")
        print(f"Your total score: {self.score}/{len(self.riddles)}. Not bad!")
        print("\nSummary:")
        for question, guess, correct in self.results:
            result = "Correct" if correct else "Incorrect"
            print(f"Riddle: {question}\nYour answer: {guess}\nResult: {result}\n")
