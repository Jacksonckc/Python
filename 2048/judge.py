from actor import Actor
import copy
# Description:

# Judge actor will determine whether the game is over, whether the move is valid thus generate the new numbers accordingly.

# OOP Principles Used:

# encapsulation, inheritance, polymorphism

# Reasoning:

# Some variables are private
# Inheriting set_tag function from it's parent.
# actor.get_instruction is used to get the instruction in the ouput class. Using actor instead of the actual class name

class Judge(Actor):
    def __init__(self):
        self._game_over = False
        self._tempBoard = []
        self.set_tag('instruction')
        self._instruction = ''
        self._no_moves = False
        self._is_won = False

    # Getting for game status.
    def get_game_status(self):
        return self._game_over

    # Setter for a temporary board which is used for comparsion with the new board to see whether the move was valid
    def set_temp_board(self, board):

        self._tempBoard = copy.deepcopy(board.get_board())

    # Getter for the temporary board
    def get_temp_board(self):
        return self._tempBoard

    # Function that checks if the old board and the new board are the same, thus, tells the users that the move is valid or not. Also gives the boolean to tell the program whether it should generate a new number or not.
    def if_no_moves(self, board):

        if self._tempBoard == board.get_board():
            self._instruction = 'Try a different direction!'
            self._no_moves = True
        else:
            self._instruction = 'Keep going!'
            self._no_moves = False

    # Getter for the move validation 
    def get_move_status(self):
        return self._no_moves

    # Getter for instruction
    def get_instruction(self):
        return self._instruction

    # Function that will determine whether the game is over
    def determine_is_won(self, board):
        # Look throught the rows to find if there is a 2048 on the board. 
        for row in board.get_board():
            if 2048 in row:
                self._is_won = True
                self._game_over = True
                self._instruction = 'You won!'


        