from board import Board
from output import Output
from mergeAction import MergeAction
from getInputAction import GetInputAction
from newNumberAction import NewNumberAction
from instruction import Instruction
from judge import Judge

# Description:

# This class directs the game follow using start_game function with a while loop

# OOP Principles Used:

# Abstraction

# Reasoning:

# This class uses abstraction because all the function calls are quite easy to understand in turns of their functionalities without gettinng indepth with what exactly each function does. 
class Director:
    def __init__(self):
        self.board = Board()
        self.output = Output()
        self.getInputAction = GetInputAction()
        self.newNumberAction = NewNumberAction(self.board)
        self.mergeAction = MergeAction(self.board)
        self.instruction = Instruction()
        self.judge = Judge()
        self.start_game()

    def start_game(self):
        # Initialize the instruction and the board
        self.instruction.create_start_instruction()
        self.output.display(self.instruction)
        self.board.create_board()

        # Game loop, if the game status is not over, then the while loop continues
        while self.judge.get_game_status() == False:
            # Only when the move input from the user is valid, the board will generate new numbers
            if self.judge.get_move_status() == False:
                self.newNumberAction.execute()
            self.output.display(self.board)
            # Saving a temporary board for comparision with the board after merges.
            self.judge.set_temp_board(self.board)

            # Merge action will take place according the the input of the user.
            self.mergeAction.execute(self.getInputAction.execute())

            # Using the temporary board to compare the current board to see if the user input is valid.
            self.judge.if_no_moves(self.board)

            # Check is the game is over.
            self.judge.determine_is_won(self.board)
         
            # Display an instruction to the user.
            self.output.display(self.judge)
        # Display the board when the game is over.
        self.output.display(self.board)


director = Director()
