import RiddleGame
import re



def levenshtein_distance(str1, str2):
  """Calculates the Levenshtein distance between two strings.

  Args:
    str1: The first string.
    str2: The second string.

  Returns:
    The Levenshtein distance between the two strings.
  """

  riddle_file = "riddles.txt"
  r = RiddleGame.RiddleGame(riddle_file)
  m = len(str1)
  n = len(r.answer)

  # Create a matrix to store the distances
  dp = [[0] * (n + 1) for _ in range(m + 1)]

  # Fill the first row and column
  for i in range(m + 1):
    dp[i][0] = i
  for j in range(n + 1):
    dp[0][j] = j

  # Fill the rest of the matrix
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if str1[i - 1] == str2[j - 1]:
        cost = 0
      else:
        cost = 1
      dp[i][j] = min(dp[i - 1][j] + 1,  # deletion
                     dp[i][j - 1] + 1,  # insertion
                     dp[i - 1][j - 1] + cost)  # substitution

  return dp[m][n]


class Riddle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def check_answer(self, guess):
        a = re.compile(rf"{self.answer.lower()}")
        str(a)
        ld = levenshtein_distance(guess, a)
        print(f"ld")
        return a.search(guess.lower())


class Math:
    def __init__(self, expression, solution):
        self.expression = expression
        self.solution = solution

    def check_solution(self, guess):
        pass
