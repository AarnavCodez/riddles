class DbConnection:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_riddles(self):
        try:
            with open(self.file_name, 'r') as file:
                return file.read().splitlines()
        except FileNotFoundError:
            print(f"The file {self.file_name} was not found.")