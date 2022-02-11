from time import sleep
from game import constants

# Game constructor
class Director:
   
    # initializing the cast members and the actions they need to perform
    def __init__(self, cast, script):
       
        self._cast = cast
        self._script = script

    # Loop through the actions.
    def start_game(self):

        while True:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")
            sleep(constants.FRAME_LENGTH)
    # call a set of actions.
    def _cue_action(self, tag):
        
        for action in self._script[tag]:
            action.execute(self._cast)
