import random

class Board:
    def __init__(self):
        self.space = "   "
        self.wall = "|"
        self.floor = "-----------"
        self.row = (self.space + self.wall) * 2 + self.space
        self.turn_dict = {}
        for i in range(9):
            self.turn_dict[i+1] = self.space
        self.game_over = False
        self.player_1_winner = False
        self.player_2_winner = False

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

    def check_combo(self):
        add_num = 1
        winning_numbers = [1, 2, 3, 4, 7]
        start_num_dict = {
            1: [1, 4, 7],
            2: [3],
            3: [1, 2, 3],
            4: [1]
        }
        while add_num <= 4:
            for i in winning_numbers:
                if i in start_num_dict[add_num]:
                    for item in start_num_dict[add_num]:
                        current_combo = [self.turn_dict[item], 
                                        self.turn_dict[item+add_num], 
                                        self.turn_dict[item+(add_num*2)]]
                        if not self.check_win(current_combo):
                            pass
                        else:
                            self.game_over = True
                            break
            add_num += 1

    def check_win(self, combo):
        if all(move == " O " for move in combo):
            self.player_1_winner = True
            return True
        elif all(move == " X " for move in combo):
            self.player_2_winner = True
            return True
        else:
            return False

    def reset_board(self):
        self.game_over = False
        self.player_1_winner = False
        self.player_2_winner = False
        for i in range(9):
            self.turn_dict[i+1] = self.space
        
board = Board()

class Move:
    def __init__(self):
        self.turn_count = 1

    def player_turn(self, cpu_human):
        if cpu_human == 1:
            cpu = True
        else:
            cpu = False
        
        if self.turn_count <= 9:
            try:
                if self.turn_count % 2 != 0:
                    choice = int(input("Which square? (1 - 9): "))
                elif cpu:
                    choice = self.cpu_move()
                    
                if 1 <= choice <= 9:
                    if board.turn_dict[choice] != board.space:
                        print("Invalid input! Square already taken.\n")
                    else:
                        if self.turn_count % 2 != 0:
                            board.turn_dict[choice] = " O "
                            self.turn_count += 1
                            board.check_combo()
                        else:
                            board.turn_dict[choice] = " X "
                            self.turn_count += 1
                            board.check_combo()
                    board.make_board()
                else:
                    print("Invalid input! Please input a number 1-9.")
            except ValueError:
                print("Invalid input! Please input a number 1-9.")

            if board.game_over:
                if board.player_1_winner:
                    print("PLAYER 1 WINS!\n")
                elif board.player_2_winner:
                    print("PLAYER 2 WINS!\n")

            if self.turn_count == 10 and not board.game_over:
                print("DRAW!")
                board.game_over = True

    def cpu_move(self):
        turn_dict = board.turn_dict
        valid_moves = list(turn_dict.keys())
        for item in range(9):
            dict_num = item + 1            
            if turn_dict[dict_num] != board.space:
                valid_moves.remove(dict_num)
        cpu_move = random.choice(valid_moves)
        print(valid_moves)
        return(cpu_move)

move = Move()

while True:
    cpu_or_human = int(input("Do you want to play against the CPU or Player 2? (1 or 2): "))
    if cpu_or_human != 1 and cpu_or_human != 2:
        print("Invalid input! Please type either 1 or 2.")
    else:
        break

while board.game_over is False:
        if cpu_or_human == 1 or cpu_or_human == 2:
            board.make_board()
            move.player_turn(cpu_human=cpu_or_human)

        if board.game_over:
            game_continue = input("Do you want to play again? (y/n): ").lower()
            if game_continue == "y":
                board.reset_board()
                move.turn_count = 1
            elif game_continue == "n":
                print("GOODBYE")
                break