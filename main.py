class Board:
    def __init__(self):
        self.space = "   "
        self.wall = "|"
        self.floor = "-----------"
        self.row = (self.space + self.wall) * 2 + self.space
        self.turn_dict = {}
        for i in range(9):
            self.turn_dict[i+1] = self.space

    def make_board(self):
        counter = 1
        print("\n")
        for i in range(17):
            i += 1
            if i % 2 == 1 or i == 1:
                print(self.turn_dict[counter], end="")
                counter += 1
            else:
                if (i + 1) % 6 == 0:
                    print(self.wall)
                elif i % 6 == 0:
                    print(f"\n{self.floor}")
                else:
                    print(self.wall, end="")
        print("\n")

board = Board()

class Move:
    def __init__(self):
        self.player_1_turn = True
        while True:
            try:
                self.guess = int(input("Which square? (1 - 9): "))
                if 1 <= self.guess <= 9:
                    if board.turn_dict[self.guess] != board.space:
                        print("Invalid input! Square already taken.\n")
                    else:
                        if self.player_1_turn:
                            board.turn_dict[self.guess] = " O "
                            self.player_1_turn = False
                        else:
                            board.turn_dict[self.guess] = " X "
                            self.player_1_turn = True 

                        board.make_board()
                else:
                    print("Invalid input! Please input a number 1-9.")
            except ValueError:
                print("Invalid input! Please input a number 1-9.")




board.make_board()

move = Move()

board = []