import random

# TODO: Define the Thrower class here.

class Thrower:
    def __init__(self, dice):
        dice = {
            self.dice01 : dice[0],
            self.dice02 : dice[1],
            self.dice03 : dice[2],
            self.dice04 : dice[3],
            self.dice05 : dice[4]
        }
        

# The throw_dice method randomly generates five new dice values and adds them to the dice list. It also increments the num_throws attribute by one.
    def throw_dice(self):
        self.dice01 = random.randint(1,6)
        self.dice02 = random.randint(1,6)
        self.dice03 = random.randint(1,6)
        self.dice04 = random.randint(1,6)
        self.dice05 = random.randint(1,6)


# The get_points method calculates and returns the total points for the current dice. Ones are worth 100 points. Fives are worth 50 points.
    def get_point(self):
        for dice in (self.dice):
            if dice:
                total_point += 100

                return total_points


# The can_throw method determines whether or not the Thrower can throw again. It returns a boolean value that is true if the dice have at least a five, or a one, or the num_throws is greater than zero. Otherwise, it returns false.

    def can_throw(self):
        pass