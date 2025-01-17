import random


def account_login():
    pass
    # (Implement the login functionality here, as needed)


def main():
    import Riddle
    import RiddleGame
    import DbConnection

    riddle_file = 'riddles.txt'
    db_conn = DbConnection.DbConnection(riddle_file)  # Pass only required parameters
    riddles = db_conn.get_riddles()

    if riddles:
        game = RiddleGame.RiddleGame(riddle_file)  # Updated to match the constructor
        game.play()
    else:
        print("No riddles found to load the game.")


switch = True
bold = "\033[1m"
reset = "\033[0m"


def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"


color1 = rgb(0, 255, 221)
color2 = rgb(255, 0, 0)
color3 = rgb(0, 255, 0)

while switch:
    start = input(
        f"Welcome to the {bold}{color1}Riddle Game{reset}!\nType {color3}play{reset} to play!\nType {color2}exit{reset} to exit the game: ").lower().strip()
    if start == 'play':
        switch = False
        if __name__ == "__main__":
            main()
    elif start == 'exit':
        print("Closing game...")
        switch = False
        quit("Game Closed")
    else:
        print("\nNo such option. Try again\n")

