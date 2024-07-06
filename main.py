import random

correct_feedback = ['Nice, You got it!', 'Your doing great!', 'Correct answer!', "Wow, you're smart!",
                    'You\'re on the run!']
incorrect_feedback = ['Nice try, but that\'s not it', 'Incorrect answer', 'You can try again later',
                      'Sorry, that isn\'t right']

start = input("Welcome to the Riddle Game!\nType 'play' to play!: ").lower()
if start == 'play':

    class Riddle:
        def __init__(self, question, answer):
            self.question = question
            self.answer = answer
        def check_answer(self, guess):
            return self.answer.lower() == guess.lower()


    class RiddleGame:
        def __init__(self, riddle_file):
            self.riddles = self.load_riddles(riddle_file)
            self.score = 0
            self.results = []

        def load_riddles(self, riddle_file):
            riddles = []
            with open(riddle_file, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if ':' in line:
                        question, answer = line.split(':')
                        riddles.append(Riddle(question.strip(), answer.strip()))
            return riddles

        def play(self):
            print("Welcome to the Riddle Game!")
            for riddle in self.riddles:
                print("\nRiddle:")
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


    class DbConnection:
        def __init__(self, file_name):
            self.file_name = file_name

        def get_riddles(self):
            try:
                with open(self.file_name, 'r') as file:
                    return file.read().splitlines()
            except FileNotFoundError:
                print(f"The file {self.file_name} was not found.")


    def main():
        riddle_file = 'riddles.txt'
        db_conn = DbConnection(riddle_file)
        riddles = db_conn.get_riddles()

        if riddles:
            game = RiddleGame(riddle_file)
            game.play()
        else:
            print("No riddles found to load the game.")


    if __name__ == "__main__":
        main()
