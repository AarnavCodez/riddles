import random


def main():
    import Riddle
    import RiddleGame
    import DbConnection
    riddle_file = 'riddles.txt'
    db_conn = DbConnection.DbConnection(riddle_file)
    riddles = db_conn.get_riddles()

    if riddles:
        game = RiddleGame.RiddleGame(riddle_file)
        game.play()

    else:
        print("No riddles found to load the game.")


switch = True

while switch:

    start = input("Welcome to the Riddle Game!\nType 'play' to play!\nType 'exit' to exit the game: ").lower()
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



