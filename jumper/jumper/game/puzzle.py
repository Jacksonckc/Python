import random
import os

class Puzzle:
    def __init__(self):
        self.list = ['apple', 'banana', 'peach', 'lemon']
        self.guess =[]
        self.word =''
        pass

    # read the txt file
    def readTxt(self):
        print (os.getcwd())
        f = open('./list.txt', 'r')
        content = f.read()
        print(content)
        f.close()


    # ramdomly selects a word from the list
    def pick_a_word(self):
        self.word = random.choice(self.list)
     

    # create the spaces for the puzzle
    def initialize_puzzle(self):
        self.pick_a_word()
        length = len(self.word)

        for i in range(length):
            self.guess.append('_')

    # regenerate the puzzle
    def formulate_puzzle(self, input):
        if self.word.find(input) >= 0:
            for i in range(len(self.word)):
                if self.word[i] == input:
                    self.guess[i] = input
            return True     
        else: return False
    
    # detect to see if the puzzle was solved
    def puzzle_solved(self):
        count = 0
        for i in range(len(self.word)):
            if self.word[i] != self.guess[i]:
                count += 1

        if count != 0:
            return False 
        else:
            return True
            
    # prints the curretn state of the puzzle
    def printPuzzle(self, input):
        self.formulate_puzzle(input)
        for i in self.guess:
            print(i, end='')


    # validate user input
    def check_input(self, input):
        if self.word.find(input) < 0:
            print('\nOops, wrong guess! Try again! ')
            return False
        else: 
            print('\nYou are one step closer! Keep it up!')
