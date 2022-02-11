from game import constants
from game.point import Point

# The parent class for word, score and buffer, which records the location and the text for the children classes
class Actor:

    def __init__(self):
  
        self._text = ""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        
    # returns the position
    def get_position(self):
      
        return self._position
    
    # returns the text
    def get_text(self):
      
        return self._text

    # returns a Point(x,y), which x is the velocity on the x axis and y is the velocity on the y axis
    def get_velocity(self):
        
        return self._velocity
    
    # changes the location for a word using it's velocity
    def move_next(self):
    
        x1 = self._position.get_x()
        y1 = self._position.get_y()
        x2 = self._velocity.get_x()
        y2 = self._velocity.get_y()
        x = 1 + (x1 + x2 - 1) % (constants.MAX_X - 1)
        y = 1 + (y1 + y2 - 1) % (constants.MAX_Y - 1)
        position = Point(x, y)
        self._position = position
    
    
    def set_position(self, position):
       
        self._position = position
    
    def set_text(self, text):
        
        self._text = text

    def set_velocity(self, velocity):
       
        self._velocity = velocity