from actor import Actor

# Description:

# Shows instructions to the users at the beginning or mid game

# OOP Principles Used:

# encapsulation, inheritance, polymorphism

# Reasoning:

# Uses set_tag function from the parent class.
# Some variables are private variables. 
# actor.get_instruction is used to get the instruction in the ouput class. Using actor instead of the actual class name

class Instruction(Actor):
    def __init__(self):
        super().__init__()
        # Tag is used in the output class for it to determine how to display the actor
        self.set_tag('instruction')
        self._instruction = ''

    # Initialize starting instruciton
    def create_start_instruction(self):
        self._instruction = 'Welcome to 2048! Your goal is to get to 2048 using the numbers appear on the board. You will have 2 randomly generated number each round, they could be 2, 4 or 8. Input a to merge left, d to merge right, w to merge up and s to merge down. Good luck!'

    # Getter for instruction.
    def get_instruction(self):
        return self._instruction