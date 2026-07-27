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

    # Creates the game board. It keeps track of which spaces have already been played by using the turn_dict.
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
        # All the winning combinations start with these numbers.
        winning_numbers = [1, 2, 3, 4, 7]
        # The keys are the numbers to add the numbers in the list by. E.g. If the key is 2, then 3, 5, 7 is a winning combo.
        add_num_dict = {
            1: [1, 4, 7],
            2: [3],
            3: [1, 2, 3],
            4: [1]
        }
        # Checks if any of the winning combos have been fulfilled.
        while add_num <= 4:
            for i in winning_numbers:
                if i in add_num_dict[add_num]:
                    for item in add_num_dict[add_num]:
                        current_combo = [self.turn_dict[item], 
                                        self.turn_dict[item+add_num], 
                                        self.turn_dict[item+(add_num*2)]]
                        # Checks if a winning combo has three X's or O's
                        if not self.check_win(current_combo):
                            pass
                        else:
                            self.game_over = True
                            break
            add_num += 1

    # Checks if a winning combo has three X's or O's
    def check_win(self, combo):
        if all(move == " O " for move in combo):
            self.player_1_winner = True
            return True
        elif all(move == " X " for move in combo):
            self.player_2_winner = True
            return True
        else:
            return False

    # Resets the board if the player wants to play again.
    def reset_board(self):
        self.game_over = False
        self.player_1_winner = False
        self.player_2_winner = False
        for i in range(9):
            self.turn_dict[i+1] = self.space
        
board = Board()

# Controls the player's/computer's moves.
class Move:
    def __init__(self):
        self.turn_count = 1

    def player_turn(self, cpu_human, cpu_mode):
        # Checks if the player wants to play against a CPU or Player 2.
        if cpu_human == 1:
            cpu = True
        else:
            cpu = False

        # Asks player to make a move, and automatically makes the CPU move once the player has chosen a move.
        if self.turn_count <= 9:
            try:
                if cpu:
                    if cpu_mode == "easy":
                        choice = self.cpu_move_easy()
                    elif cpu_mode == "hard":
                        choice = self.cpu_move_hard()
                else:
                    choice = int(input("Which square? (1 - 9): "))
                    
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

            # Checks if a player has won, or if there is draw.
            if board.game_over:
                if board.player_1_winner:
                    print("PLAYER 1 WINS!\n")
                elif board.player_2_winner:
                    print("PLAYER 2 WINS!\n")

            if self.turn_count == 10 and not board.game_over:
                print("DRAW!")
                board.game_over = True

# Easy mode: the CPU choses a random space in out of all available spaces.
    def cpu_move_easy(self):
        turn_dict = board.turn_dict
        valid_moves = list(turn_dict.keys())
        for item in range(9):
            dict_num = item + 1            
            if turn_dict[dict_num] != board.space:
                valid_moves.remove(dict_num)
        cpu_move = random.choice(valid_moves)
        print(valid_moves)
        return(cpu_move)

# Hard mode: the CPU will block any spaces that allow the player to win the next turn.
#            Otherwise, the CPU will choose a move which sets itself up for a win.
# NEED TO IMPLEMENT
    def cpu_move_hard(self):
        pass

move = Move()

# Asks the user how they would like to play the game.
while True:
    cpu_or_human = int(input("Do you want to play against the CPU or Player 2? (1 or 2): "))
    cpu_mode = None
    if cpu_or_human != 1 and cpu_or_human != 2:
        print("Invalid input! Please type either 1 or 2.")
    else:
        if cpu_or_human == 1:
            while True:
                cpu_mode = input("Choose difficulty: easy/hard?: ").lower()
                if cpu_mode != "easy" and cpu_mode != "hard":
                    print("Invalid input! Please type 'easy' or 'hard'.")
                else:
                    break
        break

# Keeps looping the game as long as the user wishes to play.
while board.game_over is False:
        if cpu_or_human == 1 or cpu_or_human == 2:
            board.make_board()
            move.player_turn(cpu_human=cpu_or_human, cpu_mode=cpu_mode)

        if board.game_over:
            game_continue = input("Do you want to play again? (y/n): ").lower()
            if game_continue == "y":
                board.reset_board()
                move.turn_count = 1
            elif game_continue == "n":
                print("GOODBYE")
                break