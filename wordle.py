import math
import random

class Wordle:
    """ Wordle state class """ 

    def __init__(self):
        self.wordle = self.load_wordle('enable1.txt')
        print(self.wordle)

    def load_wordle(self, dictionary_path):
        # Pick a wordle from the dictionary
        valid_words = []
        with open(dictionary_path) as f:
            dictionary = f.readlines()
            for word in dictionary:
                word = word.strip("\n")
                if len(word) == 5:
                    valid_words.append(word)
        
        return valid_words[math.ceil(random.random() * len(valid_words))]

wordle_state = Wordle()
