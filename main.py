import random



start = input("Welcome to the Riddle Game!\nType 'play' to play!: ").lower()
if start == 'play':



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


    if __name__ == "__main__":
        main()
