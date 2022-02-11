from game import constants
import random
from game.actor import Actor
from game.point import Point

class Word(Actor):
    def __init__(self):

        super().__init__()
        self._list = None
        self._form_list()
        self._word = ''
        self._form_word()
        position = self.form_position()
        self.set_position(position)
        self.set_text(self._word)
        
    
    def form_position(self):
        
        x = random.randint(2, constants.MAX_X - len(self._word)-1)
        y = random.randint(2, constants.MAX_Y - 2)
        position = Point(x,y)
        return position

    def _form_list(self):
        self._list = constants.LIBRARY


    def _form_word(self):

        self._word = random.choice(self._list)

        

    def changeDV(self):
        x = random.randint(-4, 4)
        y = random.randint(-4, 4)
        velocity = Point(x, y)
        self.set_velocity(velocity)

    def reset_word(self):
        self._form_word()
        self.set_text(self._word)

