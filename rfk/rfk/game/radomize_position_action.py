from game.action import Action
import random
from game.point import Point
from game import constants
class RandomizePositionAction(Action):
    def execute(self, cast):
        if random.randint(0, 100) != 100:
            return

        for artifact in cast["artifact"]:
            self._points = random.randint(1, 5)
            x = random.randint(1, constants.MAX_X - 2)
            y = random.randint(1, constants.MAX_Y - 2)
            position = Point(x, y)
            artifact.set_position(position)