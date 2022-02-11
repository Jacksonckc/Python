from numberLength import NumberLength


# Description:

# This class prints the actors, according to the tag.

# OOP Principles Used:

# Not in this class



class Output:
    def __init__(self):
        self.numLength = NumberLength()

    def display(self, actor):
        if actor.get_tag() == 'board':
            self.numLength.findTheLargestNumberLength(actor.get_board())
            numLength = self.numLength.get_largestNumLenghth()
            for row in actor.get_board():
                currentRow = '|'
                for number in row:
                    if number == 0:
                        currentRow += ' ' * numLength + '|'
                    else:
                        currentRow += ' ' * (numLength - len(str(number))) + str(number) + '|' 
                print(currentRow)
            print()
        
        elif actor.get_tag() == 'instruction':
            print(actor.get_instruction()) 
        