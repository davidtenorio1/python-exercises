# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
user_input = input("Is your input 2? Type something:")
def is_two(x):
    if x == 2: 
        return True
    elif x in "2":
        return True
    else:
        return False
test = is_two(user_input)
print(test)
    
# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(x):
    if x in "aeiouAEIOU":
        return True
    else:
        return False

user_input = input("Is your input a vowel? Type something:")
test= is_vowel(user_input)
print(test)

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_constant(x):
    if x not in "aeiouAEIOU":
        return True
    else:
        return False

user_input = input("Is your input a constant? Type something:")
test= is_constant(user_input)
print(test)

# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def capitalize_if_constant (x):
    if (x[0]) in "AEIOUaeiou":
        return x
    else:
        return x.capitalize()

user_input = input("Type something and I may or may not capitalize it:")
test= capitalize_if_constant(user_input)
print(test)

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
print("I will help you calculate the tip amount")
total_input = input("What is the bill total?")
total_in_dollars = float(total_input)
tip_input = input("What percent tip would you like to leave? (a number between 0 and 1)")
tip_percentage = float(tip_input)

def calculate_tip_amount (x,y):
    return x * y
print(calculate_tip_amount(total_in_dollars,tip_percentage))

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
