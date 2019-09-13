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
    return x in "aeiouAEIOU"

user_input = input("Is your input a vowel? Type something:")
test= is_vowel(user_input)
print(test)

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_constant(x):
    return x not in "aeiouAEIOU"

user_input = input("Is your input a constant? Type something:")
test= is_constant(user_input)
print(test)

# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def capitalize_if_constant (x):
    if (x[0]) in "AEIOUaeiou":
        return x
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
print("I will calculate the price after discount")
price_input = input("Enter the original price:")
price = float(price_input)
discount_percentage = input("Enter the discount percentage from 0 to 1:")
discount = float(discount_percentage)

def apply_discount(original_price,discount_percentage):
    return original_price * (1-discount_percentage)

price_after_discount = apply_discount(price,discount)
print(f'The price after discount is {price_after_discount}. What a deal!')

# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
user_input = input("Enter a number with commas and I will remove the commas:")
def handle_commas(s):
    return float(s.replace(",", ""))
no_commas = handle_commas(user_input)
print(no_commas)

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
user_input = input("Enter your numberic grade and I will convert to a letter grade:")
user_grade_int = int(user_input)
def get_letter_grade(s):
    if s >= 90:
        return "A"
    elif s>= 80:
        return "B"
    elif s>=70:
        return "C"
    elif s>60:
        return "D"
    else:
        return "F"
print(get_letter_grade(user_grade_int))

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
print("I am the vowel monster and I eat all vowels!")
user_input = input("Enter your word:")
def remove_vowels(word):
    letters = []
    for char in word:
        if char not in 'aeiouAEIOU':
            letters.append(char)
    return ''.join(letters)

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
def normalize_name(name):
    for c in ['!', '@', '#', '$', '%', '^', '&', '*']:
            name = name.replace(c, "")
    name = name.strip()
    name = name.lower()
    name = name.replace(" ", "_")
    return name

# 11. Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

def cumsum(xs):
    sums = [xs[0]]
    for x in xs[1:]:
        sums.append(sums[-1] + x)
    return sums

# Bonus 1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.


# Bonus 2. Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.


