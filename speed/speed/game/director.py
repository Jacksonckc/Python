from time import sleep
from game import constants
from game.buffer import Buffer
from game.score import Score
from game.word import Word
from game.judge import Judge

class Director:
    
    # preparing for the board/game
    def __init__(self, input_service, output_service):
        
        self._keep_playing = True
        self._input_service = input_service
        self._score = Score()
        
        self._words = [Word(), Word(), Word(), Word(), Word()]


        self._buffer = Buffer()
        self._judge = Judge()
        self._output_service = output_service
        
    # loops for the game functionalities
    def start_game(self):
        
        while self._keep_playing:
            
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    # sets the buffer = input from the user
    def _get_inputs(self):
        self._buffer.add_buffer(self._input_service.get_letter())
        pass

    # move the words, reset the buffer
    def _do_updates(self):
        for i in self._words:
            i.changeDV()
            i.move_next()

            iscorrect = self._judge.judge_correctness(self._buffer.get_text(), i.get_text())
            if iscorrect == True:
                self._handle_input_correctness(5)
                i.reset_word()
                self._buffer.clear_buffer()
            else:
                self._handle_input_correctness(0)

       

    # Prints the score, words and buffer on the screen
    def _do_outputs(self):
        
        self._output_service.clear_screen() #clear_buffer()
        self._output_service.draw_actor(self._score)
        for i in self._words:
            self._output_service.draw_actor(i)
        self._output_service.draw_actor(self._buffer)
        self._output_service.flush_buffer()


    # Adds points if buffer = a word
    def _handle_input_correctness(self, reward):
        self._score.add_points(reward) #passing in a point that you get from right guessing.
        # clear the buffer and reset the word
        
        pass
