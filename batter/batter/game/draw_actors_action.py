from game.action import Action

# using output service to print out all the actors to the screen
class DrawActorsAction(Action):

    # prepare for the output service
    def __init__(self, output_service):
        
        self._output_service = output_service

    #  sending current actors to the output service for it to output.
    def execute(self, cast):
       
        self._output_service.clear_screen()
        for group in cast.values():
            self._output_service.draw_actors(group)
        self._output_service.flush_buffer()