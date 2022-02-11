import sys
from game.point import Point
from asciimatics.event import KeyboardEvent

# gets the user input 
class InputService:

    # set up keys 
    def __init__(self, screen):

        self._screen = screen
        self._keys = {}
        self._keys[119] = Point(0, -1) # w
        self._keys[115] = Point(0, 1) # s
        self._keys[97] = Point(-1, 0) # a
        self._keys[100] = Point(1, 0) # d

    #  get the directions according to the input.
    def get_direction(self):
        
        direction = Point(0, 0)
        event = self._screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code == -1:
                sys.exit()
            direction = self._keys.get(event.key_code, Point(0, 0))
        return direction