from game.person import Person
from game.rope import Rope
from game.puzzle import Puzzle
from game.player import Player

class Director:
    def __init__(self):
        self.puzzle = Puzzle()
        self.rope = Rope()
        self.person = Person()
        self.player = Player()
        self.exsit = True
        self.have_rope = True
        pass

# starts the game, called by main
    def start_game(self):
        self.puzzle.initialize_puzzle()
        print("let's get started with the game shall we? ")
        while True:
            # self.puzzle.readTxt()
            input = self.player.get_input()      
            self.puzzle.printPuzzle(input)
            self.exsit = self.puzzle.check_input(input)
            self.rope.printRope(self.exsit)
            self.have_rope = self.rope.have_rope()
            if self.have_rope == False:
                self.person.printPerson(self.have_rope)
                break
            self.person.printPerson(self.have_rope)
            if self.puzzle.puzzle_solved() == True:
                print('Aw! You made it! ')
                break
            # self.again()

# tried to make it work but I struggled with it 
    def again(self):
        play_again = self.player.play_again()
        if play_again == True:
            self.start_game()
                


            
                