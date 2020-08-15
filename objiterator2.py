"""
yield returns an ITERATOR OBJECT that can be used in the __iter__ method invoked during an iteration
"""

class stupidIter:
    alphabet = ["a","b","c","d","e","f","g","h","i","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
    def __init__(self,n=0):
        self.__end = n
    
    def __iter__(self):
        print("I am an ITERATOR!")
        for i in range(self.__end):
            yield self.alphabet[i]
"""    
    def __next__(self):
        for i in range(self.__end):
            yield self.alphabet[i]
"""
for letter in stupidIter(3):
    print(letter)