from game.user import User
import random

# The game controller
class Dealer:
    def __init__(self):
        self.c_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.p_card = 0
        self.c_card = random.choice(self.c_cards)
        self.c_point = 300
        self.user01 = User()
        # True is higher and False is lower
        self.higher = False

# The whole game flow which will be called by the main file
    def start_game(self):
        
        while self.user01.play_again and self.c_point > 0:
            print('Welcome to HighLo!')
            self.show_score()
            self.get_card()
            self.get_point()
            self.show_score()

            # Validate the input
            while True:
                yesOrNo = input('Keep playing? [y/n]: ').lower()
                if yesOrNo == 'y':
                    self.user01.play_again = True
                    print('Next game it is!')
                    break
                elif yesOrNo == 'n':
                    self.user01.play_again = False
                    break
                else:
                    print('Invalid input, try again!')
            print('')
        print('Oops, the game is over')     
        pass

# Getting cards for the game, initial one and the one next to it
    def get_card(self):

        # show the first card
        self.p_card = self.c_card
        print(f'The card is: {self.p_card}')
        
        # Get the input from the user
        self.user01.get_input()
        self.c_card = random.choice(self.c_cards)
        print(f'The Next card: {self.c_card}')
        if self.c_card > self.p_card:
            self.higher = True
        else:
            self.higher = False


# Calculate the points of the users by the answers they gave
    def get_point(self):

        if self.higher == self.user01.guess:
            self.c_point += 100
        else:
            self.c_point -= 75
    
# Show the accumulative points
    def show_score(self):
        print(f'Your score is: {self.c_point}')
        pass
