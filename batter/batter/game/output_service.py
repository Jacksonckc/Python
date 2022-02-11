import sys
from game import constants
from asciimatics.widgets import Frame


#  puts the current states of all the actors on the screen
class OutputService:

    # creates the screen
    def __init__(self, screen):

        self._screen = screen

    # clear the screen every frame to prepare for the next frame
    def clear_screen(self):

        self._screen.clear_buffer(7, 0, 0)
        self._screen.print_at("-" * constants.MAX_X, 0, 0, 7)
        self._screen.print_at("-" * constants.MAX_X, 0, constants.MAX_Y, 7)

    # show all the actors on the screen
    def draw_actor(self, actor):

        text = actor.get_text()
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        if actor.get_tag() == 'paddle':
            self._screen.print_at(text, x, y, 4)  # WHITE
        else:
            self._screen.print_at(text, x, y, 5)  # WHITE

    # call the draw_actor function to output each actor
    def draw_actors(self, actors):

        for actor in actors:
            self.draw_actor(actor)

    def flush_buffer(self):

        self._screen.refresh()
