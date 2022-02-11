class Judge:
    # returns a boolean value depending on whether buffer == a word
    def judge_correctness(self, buffer, word):
        if buffer == 'Buffer: ' + word:
            return True
        else: 
            return False

