from game import constants
from game.point import Point

# An object that performs actions
class Actor:
    
    # Prepare for the actor
    def __init__(self):
        self._text = ""
        self._tag = ''
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    # get the position of the actor, an instance of class point
    def get_position(self):
        
        return self._position
    # get the text of the actor, what is needed to be shown
    def get_text(self):
       
        return self._text

    # get the direction and the velocity of the actor, an instance of class point
    def get_velocity(self):
      
        return self._velocity

    # get what the actor is 
    def get_tag(self):
        return self._tag
    
    # set the x velocity of the actor only
    def set_velocity_x(self, item, new_x):
        item.set_velocity(Point(new_x, item.get_velocity_y()))
    
    # set the y velocity of the actor only
    def set_velocity_y(self, item, new_y):
        item.set_velocity(Point(item.get_velocity_x(),new_y))

    # get the x velocity of the actor only
    def get_velocity_x(self):
        return self._velocity.get_x()

    # get the y velocity of the actor only
    def get_velocity_y(self):
        return self._velocity.get_y()

    # get the x position of the actor only
    def get_position_x(self):
        return self._position.get_x()

    # get the y position of the actor only
    def get_position_y(self):
        return self._position.get_y()

    # set x,y position, arguement position is a point class.
    def set_position(self, position):
        
        self._position = position
    
    # set text of the actor
    def set_text(self, text):
        
        self._text = text

    # set velocity of the actor, arguement velocity is a point class.
    def set_velocity(self, velocity):
        
        self._velocity = velocity

    # give the actor a category or name.
    def set_tag(self, tag):
        self._tag = tag