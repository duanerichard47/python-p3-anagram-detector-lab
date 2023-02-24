# your code goes here!
class Anagram:

    def __init__(self,word):
        self.word = word
        pass

    def match(self,word, a_list):
        word_backwards = word[::-1]
        self.a_list = []
        if word_backwards in  self.a_list: 
        return a_list