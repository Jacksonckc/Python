import random
from game.actor import Actor
from game.point import Point

class Score(Actor):
    """This class will create a score class and set it in the top left of the
        screen."""
    
    # initialize the position of the score, and the text
    def __init__(self):
       
        super().__init__()
        self._points = 0 #default score
        position = Point(1, 0)
        self.set_position(position)
    """Will rack up points and update the score"""
    # called in diretor
    def add_points(self, points):
        self._points += points
        self.set_text(f"Score: {self._points}")