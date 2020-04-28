from random import *

def weirdTalk(sentence):
    newSentence = sentence.lower().split()
    output = ''
    randomNum = 1
    for word in newSentence:
        for char in word:
            randomNum = randint(1,2)
            if randomNum == 1 :
                output += char.capitalize()
            else:
                output += char
        output += ' '
    return output