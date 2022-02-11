# The current position of an actor
class Point:

    # initializing x and y positions.
    def __init__(self, x, y):

        self._x = x
        self._y = y

    # check if two points have the same position

    def equals(self, other):

        return self._x == other.get_x() and self._y == other.get_y()

    # get the x value of the position
    def get_x(self):

        return self._x

    # get the y value of the position
    def get_y(self):

        return self._y

    # check in a position is at x=0 y=0
    def is_zero(self):

        return self._x == 0 and self._y == 0
