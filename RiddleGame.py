import random
import Riddle
import time
import argparse

class RiddleGame:
    def __init__(self, riddle_file, question_count):
        """
        Initialize the RiddleGame.

        :param riddle_file: Path to the file containing riddles.
        :param question_count: Number of riddles to present during the game.
        """
        self.riddles = self.load_riddles(riddle_file)
        self.question_count = min(question_count, len(self.riddles))  # Limit to available riddles
        self.score = 0
        self.results = []
        self.correct_feedback = [
            'Nice, you got it!',
            'You’re doing great!',
            'Correct answer!',
            "Wow, you're smart!",
            'You’re on the run!'
        ]
        self.incorrect_feedback = [
            'Nice try, but that’s not it',
            'Incorrect answer',
            'You can try again later',
            'Sorry, that isn’t right'
        ]

    def load_riddles(self, riddle_file):
        """Load riddles from a file."""
        riddles = []
        try:
            with open(riddle_file, 'r') as file:
                for line in file:
                    if ':' in line:
                        question, answer = line.strip().split(':', 1)
                        riddles.append(Riddle.Riddle(question.strip(), answer.strip()))
        except FileNotFoundError:
            print(f"The file {riddle_file} was not found.")
        return riddles

    def play(self):
        """Play the game with riddles."""
        if not self.riddles:
            print("No riddles found. Exiting game.")
            return

        print(f"Welcome to the Riddle Game! You will be asked {self.question_count} questions.")
        random.shuffle(self.riddles)  # Shuffle riddles for randomness
        selected_riddles = self.riddles[:self.question_count]

        global start
        start = time.time()

        for item in selected_riddles:
            self.ask_question(item)

        global end
        end = time.time()
        self.show_summary()

    def ask_question(self, item):
        """Ask a single question and handle user response."""
        print("\nQuestion:")
        print(item.get_question())

        while True:
            guess = input("Your answer (type 'skip' to skip or 'hint' for a hint): ").strip().lower()
            if not guess:
                print("Please enter an answer, 'skip', or 'hint'.")
                continue

            if guess == "skip":
                print(f"You skipped the question. The correct answer was: {item.answer}")
                self.results.append((item.get_question(), "Skipped", False))
                break

            if guess == "hint":
                self.give_hint(item)
                continue

            correct = item.check_answer(guess)
            if correct:
                print(random.choice(self.correct_feedback))
                self.score += 1
                self.results.append((item.get_question(), guess, True))
                break
            else:
                print(random.choice(self.incorrect_feedback))
                self.results.append((item.get_question(), guess, False))
                break

    def give_hint(self, item):
        """Provide a hint for the riddle."""
        hint = item.answer[0] + "..." + item.answer[-1]
        print(f"Hint: {hint} (The answer starts and ends with these letters)")

    def show_summary(self):
        """Show the final summary of the game."""
        print("\nGame Over!")
        print(f"Your total score: {self.score}/{self.question_count}. Great job!")
        print(f"You took {round(end - start, 1)} seconds to finish.")
        print("\nSummary:")
        for question, guess, correct in self.results:
            result = "Correct" if correct else "Incorrect" if guess != "Skipped" else "Skipped"
            print(f"Question: {question}\nYour answer: {guess}\nResult: {result}\n")


# CLI Application
def main():
    parser = argparse.ArgumentParser(description="Riddle Game CLI Application")
    parser.add_argument("riddle_file", help="Path to the file containing riddles (in 'question:answer' format).")
    parser.add_argument(
        "-q", "--question_count", type=int, default=5,
        help="Number of riddles to ask during the game (default: 5)."
    )

    args = parser.parse_args()

    game = RiddleGame(riddle_file=args.riddle_file, question_count=args.question_count)
    game.play()


if __name__ == "__main__":
    main()
