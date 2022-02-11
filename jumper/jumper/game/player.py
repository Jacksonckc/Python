class Player:
    def __init__(self):
        self.input = None
    

    # get input from the users
    def get_input(self):
       
        while True:
            self.input = input('Guess a letter [a-z]: ').lower()
            if len(self.input) > 1:
                print('You should only enter one letter! Try again! ')
            else:
                break
        return self.input

    # ask if they want to play again
    def play_again(self):
        while True:
            play_again = input('Do you want to play again?[y/n]: ').lower()
            if play_again == 'y':

                return True
            elif play_again == 'n': 
                return False
                
            else:
                print('Invalid input! Try again! ')