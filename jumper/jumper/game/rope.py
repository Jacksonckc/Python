class Rope:
    def __init__(self):
        self.rope = ['\n', ' ___','/___\ ', '\   /', ' \ /']

    # prints the current state of the rope
    def printRope(self, exist):
        self.cut_rope(exist)
        for i in self.rope:
            print(i)


    # cuts the rope when a wrong input
    def cut_rope(self, exist):

        if exist == False:
            self.rope.pop(1)

    # checks if there is still rope left
    def have_rope(self):
        if len(self.rope) == 1:
            return False
        else:
            return True