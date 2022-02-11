import random
from typing import Counter

# TODO: Define the Board class here


class Board():
    def __init__(self):
        self._answer = []
        self._display = [[], []]
        self._guess = []
        self.digits = 0
        self._prepare()
        self._count = 0
        self._count2 = 1
        self.guess_board01 = ['----']
        self.guess_board02 = ['----']


    # Apply the guess in the board
    def apply(self, guess, player):
        guess = str(guess.get_guess())
        
        for i in guess:
            self._guess.append(int(i))
        

        for i in range(len(self._guess)):
            # set all items back to * in display
            self._display[player][i] = "*"

            # loop through to put o in display 
            for j in range(len(self._answer)):
                if self._answer[j] == self._guess[i]:
                    self._display[player][i] = 'o'
                    # loop through to put x in display
                    for i in range(len(self._answer)):
                        if self._answer[i] == self._guess[i]:
                            self._display[player][i] = "x"            
        # reset _guess for the next player
        self._guess = []

    # see if display has all x, if yes, games over
    def all_x(self, player):

        for i in self._display[player]:
            if i != "x":
                return False
        return True

    # transforms display into board
    def to_string(self, names, guess):
        
        if self._count%2 == 1:
            self.guess_board01.append(str(guess))
            
        else:
            self.guess_board02.append(str(guess))


        text = "\n--------------------"
        for index, i in enumerate(self._display):
            
            text += "\nPlayer " 
            text += str(names[index])
            text += ': '
            
            if self._count2%2 == 1:
                text += self.guess_board01[-1]
                text += ', '
            else:
                text += self.guess_board02[-1]
                text += ', '
            self._count2 += 1

            # for a in range(len(str(guess))):
            #     text += str(guess)[a]


            for j in range(len(i)):
                text += i[j]
        text += "\n--------------------"
        self._count += 1
        return text

    # set up a number to guess, the initial display board
    def _prepare(self):
        self.digits = random.randint(4, 6)
        for n in range(self.digits):
            number = random.randint(1, 9)
            self._answer.append(number)

        for n in range(len(self._display)):
            for i in range(len(self._answer)):
                self._display[n].append('*')


    