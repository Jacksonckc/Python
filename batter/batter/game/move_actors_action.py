from game import constants
from game.action import Action
from game.point import Point

# changes the positions of the actors according to the updates.
class MoveActorsAction(Action):
   
    # loop through all the actors and change all the positions if there is a change.
    def execute(self, cast):
        
        for group in cast.values():
            for actor in group:
                if not actor.get_velocity().is_zero():
                    self._move_actor(actor)

    # change the position for one actor.
    def _move_actor(self, actor):
        
        position = actor.get_position()
        velocity = actor.get_velocity()
        x1 = position.get_x()
        y1 = position.get_y()
        x2 = velocity.get_x()
        y2 = velocity.get_y()
        if actor.get_tag() == 'paddle':
            x = x1 + (x2*2)
            y = y1
            if x1 == 1:
                x = x1 + 2
            elif x1 == 69:
                x = x1 -2   
            position = Point(x, y)
            actor.set_position(position)
        elif actor.get_tag() == 'ball':
            x = 1 + (x1 + x2 - 1) % (constants.MAX_X - 1)
            y = 1 + (y1 + y2 - 1) % (constants.MAX_Y - 1)
            position = Point(x, y)
            actor.set_position(position)