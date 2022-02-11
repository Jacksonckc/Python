from game import constants
from game.action import Action

# Control the actor with user's input
class ControlActorsAction(Action):
    
    # get the input
    def __init__(self, input_service):
        
        self._input_service = input_service

    # change the velocity according to the user's input.
    def execute(self, cast):
        
        direction = self._input_service.get_direction()
        paddle = cast["paddle"][0] # there's only one in the cast
        paddle.set_velocity(direction)        
