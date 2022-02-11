from action import Action

# Description:

# This class gets the user input.

# OOP Principles Used:

# Polymorphism, inheritance, encapsolation 

# Reasoning:

# GetInputAction class is a child class of action, it uses execute function inheried from action. 
# Some of the variables are only accessible here inside the class itself.
class GetInputAction(Action):
    def __init__(self):
        self._direction = None
        self.vaildInput = False

    # Modified function from the parent
    def execute(self):
        self.vaildInput = False
        # Keep looping till the input is valid
        while self.vaildInput == False:
            # Ask for input
            self._direction = input('What do you want to merge?')
            if self._direction == 's' or self._direction == 'w' or self._direction == 'a' or self._direction == 'd':
                self.vaildInput = True
            else: # Hint for the user that the input is not valid, ask for the input again.
                print('Invalid input, try again please')
        return self._direction