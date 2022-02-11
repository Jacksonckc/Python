import random

# TODO: Define the Hider class here

class Hider:
    def __init__(self):
        self.location = random.randint(1, 1000)
        self.distance = [self.location]

    def get_hint(self):
        if self.distance[-1] == 0:
            return '(;.;) You found me!'
        elif self.distance[-1] > self.distance[-2]:
            return '(^.^) Getting colder!'

        elif self.distance[-1] == self.distance[-2]:
            return '(=_=) You are the same distance from your last location.'
        else:
            return '(>.<) Getting warmer!'

    def watch(self, location):
        distance = abs(self.location - location)
        self.distance.append(distance)


    


