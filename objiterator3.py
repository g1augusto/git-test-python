class stupidIter:
    alphabet = ["a","b","c","d","e","f","g","h","i","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
    def __init__(self,n=1):
        self.__end = n-1
        self.__index = 0
    
    def __iter__(self):
        print("I am an ITERATOR!")
        return self
    
    def __next__(self):
        while self.__index < len(self.alphabet) and self.__index <= self.__end:
            letter = self.alphabet[self.__index]
            self.__index +=1
            return letter
        else:
            raise StopIteration

for letter in stupidIter(29):
    print(letter,end =' ')