with open('/usr/share/dict/words') as f:
    words = f.read().split('\n')

def five_letters(word):
    count = len(word)
    return count == 5

def letter_converter(word):
    word_counter = 0
    for letter in word:
        letter = ord(letter) - 96
        word_counter += letter
    return word_counter

def test(word):
    if five_letters(word) == False:
        return False
    if letter_converter(word[-1]) == (letter_converter(word) / 2):
        return True
    else:
        return False

for x in words:
    if test(x) == True:
        print(x)






