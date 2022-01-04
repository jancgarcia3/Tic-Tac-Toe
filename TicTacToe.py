# ---------------- Python Terminal Game: Tic-Tac-Toe -----------------------
# Written: Python 3.8.9
# Author: Jan C Garcia
# Date Created: 12/26/2021
# Version: 1.0
# Email: jancgarcia3@gmail.com
#
# In this game, you can either play against a computer player in single player or against a friend in two-player mode. 
# 
# The computer is programmed randomly and it is not set by any difficulty.
# 
# Who ever wins or ties, the program will reset the game by asking the user if they wish to play again.

import random

# The Board game class.
class Board:
    # Sets the board.
    def setup_board(self):
        self.board = ["_", "_", "_",
                      "_", "_", "_",
                      "_", "_", "_"]
    
    # Displays the board by printing it in the terminal when called.
    def display_board(self):
        print("\n" + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print(self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print(self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8] + "\n")

# The Players class. 
# Inherits the Board class methods.      
class Players(Board):
    # Constructor of the Players class.
    def __init__(self):
        self.player_1 = ""
        self.player_2 = ""
        self.computer = ""
        self.track_position = []
    
    # Input 1 or 2 for how many players are playing?
    # Returns the number of players.
    def how_many_players(self):
        number_of_players = input("How many players are playing?: ")
        while (number_of_players != "1" and number_of_players != "2"):
            number_of_players = input("How many players are playing? Only pick between 1 or 2: ")
        return number_of_players

    # Input X/x or O/o to pick your player.
    def pick_your_player(self):
        player = input("\n" + "Select your player by inputting either X/x or O/o: ")
        player = player.upper()
        while (player != "X" and player != "O"):
            player = input("Select your player by inputting either X/x or O/o: ")
            player = player.upper()
        if player == "X":
            return "X"
        else:
            return "O"

    # Handles the turn of the specific player.
    def handle_turns(self, player): 
        while True:
            try:
                if player == self.player_1:
                    self.display_board()
                    position = int(input("Player 1 enter a position from 1-9: "))
                    while (position > 9) or (position < 1):
                        self.display_board()
                        position = int(input("Player 1 enter integers only! Pick a position from 1-9: "))
                    position = position - 1
                    if position not in self.track_position:
                        self.track_position.append(position)
                        self.board[position] = player
                        break
                else:
                    self.display_board()
                    position = int(input("Player 2 enter a position from 1-9: "))
                    while (position > 9) or (position < 1):
                        position = int(input("Player 2 enter integers only! Pick a position from 1-9: " + "\n"))
                    position = position - 1
                    if position not in self.track_position:
                        self.track_position.append(position)
                        self.board[position] = player
                        break
            except:
                print("\n" + "Enter integers only! Pick a position from 1-9: ")  

    # The method for the computer to take its turn.
    # The computer turns are progrommed randomly to pick an availiable spot on the board.
    def computer_turn(self):
        # A list of numbers that will be randomly selected to be appended onto the [track_position] list.
        position_lst = []
        counter = 0
        if self.player_1 == "X":
            self.computer_player = "O"
        else:
            self.computer_player = "X"
        for place in self.board:
            if place == "_":
                # Append the values of the counter onto the list.
                position_lst.append(counter)
            # Increment the counter by 1.
            counter += 1
        # From the list [position_lst] it randomly selects a random integer between 0 and 8.
        random_position = random.choice(position_lst)
        # Append the value of the random_position onto the list that tracks all the positions on the board [track_position].
        self.track_position.append(random_position)
        # The computer player (X or O) replaces the value at that index on the board thru the integer value from [random_position].
        self.board[random_position] = self.computer_player

# The main class that inherits all methods and properties from the Player class and Board class.
class TicTacToe(Players):
    def __init__(self):
        super().__init__()
        self.winner_found = False
        self.tie_found = False
        self.random_player = 0
        self.player_1_points = 0
        self.player_2_points = 0
        self.tie_points = 0

    # Reset the variables
    def reset(self):
        self.winner_found = False
        self.tie_found = False
        self.track_position = []
        self.setup_board()
    
    # Start the game.
    def start_game(self):
        self.random_player = random.randrange(1, 3)
        self.reset()
        players = self.how_many_players()
        if players == "1":
            self.player_1 = self.pick_your_player()
            self.single_player_game(self.player_1)
        else:
            if self.random_player == 1:
                print("\n" + " --- Player 1 picks --- ")
                self.player_1 = self.pick_your_player()
                if self.player_1 == "X":
                    self.player_2 = "O"
                else:
                    self.player_2 = "X"
            else:
                print("\n" + " --- Player 2 picks --- ")
                self.player_2 = self.pick_your_player()
                if self.player_2 == "X":
                    self.player_1 = "O"
                else:
                    self.player_1 = "X"
            self.two_player_game(self.player_1, self.player_2)
        self.play_again()

    # Single player game method.
    def single_player_game(self, player):
        while (self.winner_found or self.tie_found) == False:
            self.handle_turns(player)
            self.check_results()
            if (self.winner_found or self.tie_found) == True:
                break
            self.computer_turn()
            self.check_results()

    # Two player game method.
    def two_player_game(self, player_one, player_two):
        # If the random_player was picked as 1 then player one goes first. 
        if self.random_player == 1:
            while(self.winner_found or self.tie_found) == False:
                self.handle_turns(player_one)
                self.check_results()
                if (self.winner_found or self.tie_found) == True:
                    break
                self.handle_turns(player_two)
                self.check_results()
        else:
            while(self.winner_found or self.tie_found) == False:
                self.handle_turns(player_two)
                self.check_results()
                if (self.winner_found or self.tie_found) == True:
                    break
                self.handle_turns(player_one)
                self.check_results()

    # Check the conditions to win TicTacToe.
    # The method checks for three Xs or three Os on the board.
    # Returns True if a winner is found.
    # Else False.
    def check_for_winner(self, player):
        for i in range(0,3):
            # Check for columns
            if self.board[0 + i] == self.board[3 + i] == self.board[6 + i] == player:
                self.winner_found = True
                return True

            # Check for rows
            if self.board[0 + i * 3] == self.board[1 + i * 3] == self.board[2 + i * 3] == player:
                self.winner_found = True
                return True

            # Check for diagonals
            if self.board[0] == self.board[4] == self.board[8] == player:
                self.winner_found = True
                return True
            
            if self.board[2] == self.board[4] == self.board[6] == player:
                self.winner_found = True
                return True

        return False

    # Check for a tie.
    # Returns True if a tie is found,
    def check_for_tie(self):
        if "_" not in self.board and self.winner_found == False:
            self.tie_found = True
            return True
        return False
    
    # Checks for a winner or a tie and prints out the player X or O that won.
    # Returns nothing.
    def check_results(self):
        if self.check_for_winner("X"):
            if self.player_1 == "X":
                self.player_1_points += 1
                print("\n" + "Player 1 (X) wins!: " + str(self.player_1_points))
                print("Player 2 (O): " + str(self.player_2_points))
                print("Tie: " + str(self.tie_points))
            else:
                self.player_2_points += 1
                print("\n" + "Player 1 (O): " + str(self.player_1_points))
                print("Player 2 (X) wins!: " + str(self.player_2_points))
                print("Tie: " + str(self.tie_points))
            self.display_board()
            return 
        if self.check_for_winner("O"):
            if self.player_1 == "O":
                self.player_1_points += 1
                print("\n" + "Player 1 (O) wins!: " + str(self.player_1_points))
                print("Player 2 (X): " + str(self.player_2_points))
                print("Tie: " + str(self.tie_points))
            else:
                self.player_2_points += 1
                print("\n" + "Player 1 (X): " + str(self.player_1_points))
                print("Player 2 (O) wins!: " + str(self.player_2_points))
                print("Tie: " + str(self.tie_points))
            self.display_board()
            return 
        if self.check_for_tie():
            self.tie_points += 1
            print("\n" + "It's a tie!: " + str(self.tie_points))
            print("Player 1: " + str(self.player_1_points))
            print("Player 2: " + str(self.player_2_points))
            self.display_board()
            return 
        return  

    # The method to play again.
    # A while loop to ask the user if he/she would like to play again.
    # If the input is "y" then the method [start_game()] is called again.
    # If the input is "n" then we end the program.
    def play_again(self):
        while True:
            again = input("Would you like to play again? Enter y/n: ")
            if again == "n":
                print("\n" + "Thanks for playing!")
                return
            elif again == "y":
                print("Lets play again!" + "\n")
                self.start_game()
                return
            else:
                print("\n" + "You should enter either \"y\" or \"n\"." + "\n")

# Initialize an object and starts the game.
Game = TicTacToe()
Game.start_game()
