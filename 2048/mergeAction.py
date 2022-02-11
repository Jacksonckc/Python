

from action import Action
# Description:

# Deals with all the merges according to the current board numbers and the direction from user input 

# OOP Principles Used:

# encapsulation, inheritance, polymorphism

# Reasoning:

# A child class of Action.
# Variables are private

class MergeAction(Action):
    def __init__(self, board):
        # Get the board from the generate board class
        self._board = board


    # Execute the merge according to the direction.
    def execute(self, direction):
        if direction == 'a':
            self.mergeLeft()
        elif direction == 'd':
            self.mergeRight()
        elif direction == 'w':
            self.mergeUp()
        else:
            self.mergeDown()

    # Merge only one row left
    def mergeOneRowLeft(self, row):
        # j in one item in the row, i is the number of times we want to merge that item to the left.
        for j in range(self._board.get_boardSize() - 1):
            for i in range(self._board.get_boardSize()-1, 0, -1):
                # When position i - 1 is empty, replace it with position i, set position i = empty.
                if row[i - 1] == 0:
                    row[i-1] = row[i]
                    row[i] = 0

        for i in range(self._board.get_boardSize() - 1):
            # When position i + 1 = i, they should combine, and set position i + 1 = empty
            if row[i] == row[i+1]:
                row[i] *= 2
                row[i+1] = 0

        for i in range(self._board.get_boardSize() - 1, 0, -1):
            # Merge left one more time sine the combination loop might cause some empty positions.
            if row[i - 1] == 0:
                row[i-1] = row[i]
                row[i] = 0
        # retrun the row for other merge functions to use
        return row

    # Use the tempBoard to save the changes made by merging the board to the left and use the setter to set the board.
    def mergeLeft(self):
        tempBoard = []

        for i in range(self._board.get_boardSize()):
            tempBoard.append([])
            # Loop through all the rows and merge each row to the left
            tempBoard[i] = self.mergeOneRowLeft(self._board.get_board()[i])
        self._board.set_board(tempBoard)

    # Reverses the board
    def reverse(self, row):
        tempRow = []
        for i in range(self._board.get_boardSize() - 1, -1, -1):
            tempRow.append(row[i])
        return tempRow

    def mergeRight(self):
        tempBoard = []
        for i in range(self._board.get_boardSize()):
            tempBoard.append([])
            # Use the reverse function to reverse each row on the board, and merge all the rows left, reverse them back to achieve merging the board right
            tempBoard[i] = self.reverse(self._board.get_board()[i])
            tempBoard[i] = self.mergeOneRowLeft(tempBoard[i])
            tempBoard[i] = self.reverse(tempBoard[i])

        self._board.set_board(tempBoard)

    def diagnolize(self):
        # Diagnolize the board by creating a temp number, store a position, change that position to the value that is on the diagnol side, and change the diagnol position value to the temp number.
        for j in range(self._board.get_boardSize()):

            for i in range(j, self._board.get_boardSize()):
                if i != j:

                    tempNum = self._board.get_board()[j][i]
                    self._board.set_board_byID(j, i, self._board.get_board()[i][j])
                    self._board.set_board_byID(i, j, tempNum)


    def mergeUp(self):
        # Diagnolize the board and merge the board left to achieve merging up.
        self.diagnolize()
        self.mergeLeft()
        self.diagnolize()

    def mergeDown(self):
        # Diagnolize the board and merge the board right to achieve merging down.
        self.diagnolize()
        self.mergeRight()
        self.diagnolize()
