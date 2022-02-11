# The player
class User:
    def __init__(self):
        self.guess = True
        self.play_again = True


# Provide an input for the dealer
    def get_input(self):
        
        while True:
            answer = input("Higher or lower? [h/l]: ").lower()

            if answer == 'h':
                self.guess = True
                break
            elif answer == 'l':
                self.guess = False
                break
            else:
                print("Invalid input, try again.")

        
