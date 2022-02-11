from game.actor import Actor
from game.point import Point



class Buffer(Actor):
    #initializing the buffer text and the position
    def __init__(self):
        super().__init__()
        self._buffer = ''
        position = Point(1, 20)
        self.set_position(position)
        
        self.set_text(f"Buffer: {self._buffer}")

    # should be called in director
    def add_buffer(self, letter):
        if letter == 'enter':
            self._buffer = ''
        elif letter == 'space':
            self._buffer += '_'
        elif letter == 'delete':
            self._buffer = self._buffer[:-1]
        else:
            self._buffer += letter
        
        self.set_text(f"Buffer: {self._buffer}")
    
    def clear_buffer(self):
        self._buffer = ''
        self.set_text(f"Buffer: {self._buffer}")

    

