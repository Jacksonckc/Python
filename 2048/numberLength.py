# Description:

# This class help the board to look consistent by telling the output class how much space the board need. If the greatest number of the board is 3 digit, each spot on the board should all be 3 spaces regardless of the value in the spot.

# OOP Principles Used:

# encapsulation

# Reasoning:

# One private variable is used
class NumberLength:
    def __init__(self):
        self._largestNumLength = 0

    def findTheLargestNumberLength(self, board):
        largest = board[0][0]

        for row in board:
            for number in row:
                if number > largest:
                    largest = number

        self._largestNumLength = len(str(largest))

    def get_largestNumLenghth(self):
        return self._largestNumLength
