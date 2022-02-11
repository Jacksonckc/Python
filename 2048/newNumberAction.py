import random
from action import Action
# Description:

# Generates new numbers on the board

# OOP Principles Used:

# encapsulation, inheritance, polymorphism

# Reasoning:

# A child class of Action.
# Variables are private
class NewNumberAction(Action):
    def __init__(self,board):
        self._board = board

    # Use randint function to randomly generate a number
    def generate_new_num(self):
        chance = random.randint(1,20)
        if chance == 1:
            return 8
        elif chance == range(2, 8):
            return 4
        else:
            return 2

    def execute(self):
        # Generate 2 numbers, the 2 numbers come from the generate_new_num function in this class.
        numberNeeded = 0
        count = 0
        for j in range(self._board.get_boardSize()):
            for i in range(self._board.get_boardSize()):
                if self._board.get_board()[j][i] == 0:
                    count += 1
        
        if count >= 2:
            numberNeeded = 2
        else:
            numberNeeded = count
                
        while numberNeeded > 0:
            rowNum = random.randint(0, self._board.get_boardSize() - 1)
            colNum = random.randint(0, self._board.get_boardSize() - 1)
            if self._board.get_board()[rowNum][colNum] == 0:

                self._board.set_board_byID(rowNum,colNum, self.generate_new_num())
                numberNeeded -= 1
