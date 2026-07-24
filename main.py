class Board:
    def __init__(self):
        self.space = "   "
        self.column = "|"
        self.row = "-------------"

    def make_board(self):
        print("\n")
        for i in range(2):
            row = (self.space + self.column) * 3
            print(row, "\n", self.row)
        print(row)
        print("\n")

class Move:
    def __init__(self):
        while True:
            try:
                self.guess = int(input("Which square? (1 - 9): "))
                if 1 <= self.guess <= 9:
                    break
                else:
                    print("Invalid input! Please input a number 1-9.")
            except ValueError:
                print("Invalid input! Please input a number 1-9.")


board = Board()

board.make_board()

# move = Move()

board = []