from random import randint
from actor import Actor
import random

# Description:

# child class for Actor, modifies the tag variable here.

# OOP Principles Used:

# Polymorphism, inheritance, encapsolation 

# Reasoning:

# Board class is a child class of actor, it uses tag variable inheried from actor. 
# Some of the variables are only accessible here inside the class itself.
# actor.get_instruction is used to get the instruction in the ouput class. Using actor instead of the actual class name


class Board(Actor):
    def __init__(self):
        super().__init__()
        self._boardSize = random.randint(4, 6)
        self._board = []
        self.set_tag('board')

    # Creates an empty board
    def create_board(self):
        for i in range(self._boardSize):
            row = []
            for j in range(self._boardSize):
                row.append(0)
            self._board.append(row)

    # Getter for the board
    def get_board(self):
        return(self._board)

    # Getter for the board size
    def get_boardSize(self):
        return self._boardSize

    # Setter for the board
    def set_board(self, newBoard):
        self._board = newBoard

    # A different setter for the board using j i index.
    def set_board_byID(self, j, i, newNum):
        self._board[j][i] = newNum