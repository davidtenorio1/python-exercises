print("I am the vowel monster and I eat all vowels!")
user_input = input("Enter your word:")
def remove_vowels(word):
    letters = []
    for char in word:
        if char not in 'aeiouAEIOU':
            letters.append(char)
    return ''.join(letters)
user_output = remove_vowels(user_input)
print(user_output)