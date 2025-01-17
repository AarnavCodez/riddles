class DbConnection:
    def __init__(self, riddle_file):
        self.riddle_file = riddle_file

    def get_riddles(self):
        """Get riddles from the riddles file."""
        try:
            with open(self.riddle_file, 'r') as file:
                return file.read().splitlines()
        except FileNotFoundError:
            print(f"The file {self.riddle_file} was not found.")
            return []
