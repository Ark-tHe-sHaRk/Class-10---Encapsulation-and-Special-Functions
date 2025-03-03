# Creating the class
class WordReverser:
    def __init__(self, word):
        self.word = word

    def reverse(self):
        return self.word[::-1]

# Testing the class
if __name__ == "__main__":
    word = input('What is your word? ')
    reverser = WordReverser(word)
    print('Reversed word:', reverser.reverse())