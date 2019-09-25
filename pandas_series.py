# 1.) Use pandas to create a Series from the following data:
import pandas as pd
import matplotlib.pyplot as plt

#["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
# a. Name the variable that holds the series fruits.
fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

# b. Run .describe() on the series to see what describe returns for a series of strings.
fruits.describe()

# c. Run the code necessary to produce only the unique fruit names.
fruits.unique()

# d. Determine how many times each value occurs in the series.
fruits.value_counts()

# e. Determine the most frequently occurring fruit name from the series.
print(fruits.value_counts().idxmax())

# f. Determine the least frequently occurring fruit name from the series.
print(fruits.value_counts().idxmin())

# g. Write the code to get the longest string from the fruits series.
print(fruits.str.len())
print(fruits[5])

# h. Find the fruit(s) with 5 or more letters in the name.
fruits_five_letters = fruits[fruits.str.len() > 4]
print(fruits_five_letters)

# i. Capitalize all the fruit strings in the series.
fruits_capitalized = fruits[fruits.str.capitalize()]
print(fruits_capitalized)

# j. Count the letter "a" in all the fruits (use string vectorization)
print(fruits.str.count('a').sum())

# k. Output the number of vowels in each and every fruit.
def number_of_vowels(word):
    count = 0
    for letter in word:
        if letter in 'aeiou':
            count += 1
    return count
vowel_count = fruits.apply(number_of_vowels)
print(vowel_count)

# l. Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.
multiple_o_function = lambda x: (x.count('o') > 1)
o_fruits = fruits[fruits.apply(multiple_o_function)]
print(o_fruits)

# m. Write the code to get only the fruits containing "berry" in the name
berry_fruits = fruits[fruits.str.contains('berry')]
print(berry_fruits)

# n. Write the code to get only the fruits containing "apple" in the name
apple_fruits = fruits[fruits.str.contains('apple')]
print(apple_fruits)

# o. Which fruit has the highest amount of vowels?
fruit_max_vowels = fruits[vowel_count.max()]
print(fruit_max_vowels)







# 2.) Use pandas to create a Series from the following data:
#['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
prices = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

#What is the data type of the series?
print(prices.dtype)

#Use series operations to convert the series to a numeric data type.
no_dollar_sign = prices.str.replace("$","")
no_dollar_sign_or_commas = no_dollar_sign.str.replace(",", "")
numeric_prices = pd.to_numeric(no_dollar_sign_or_commas)
print(numeric_prices)

#What is the maximum value? The minimum?
print(numeric_prices.max())
print(numeric_prices.min())

#Bin the data into 4 equally sized intervals and show how many values fall into each bin.
pd.cut(numeric_prices, 4)
#Plot a histogram of the data. Be sure to include a title and axis labels.
plt.hist(numeric_prices)
plt.suptitle("Prices")
plt.xlabel('$\$$')
plt.ylabel('$Amount$')
plt.show()







# 3.) Use pandas to create a Series from the following exam scores:
#[60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

#What is the minimum exam score? The max, mean, median?
print(exam_scores.min())
print(exam_scores.max())
print(exam_scores.mean())

#Plot a histogram of the scores.
plt.hist(exam_scores)

#Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.
def letter_grade_converter(grades):
    letter_grades = []
    for grade in grades:
        if grade >= 90:
            letter_grades.append('A')
        elif grade >= 80:
            letter_grades.append('B')
        elif grade >= 70:
            letter_grades.append('C')
        else:
            letter_grades.append('F')
    return letter_grades 

print(letter_grade_converter(exam_scores))
        
#Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, and that many points should be given to every other score as well.
highest_grade = exam_scores.max()
curve = 100 - highest_grade
curved_grade_function = lambda x : x + curve
print(exam_scores.apply(curved_grade_function))







# 4.) Use pandas to create a Series from the following string:
#'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'
original = ('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')
def split(word): 
    return [char for char in word]
new_list = split(original)  
word = pd.Series(new_list)
print(word)

#What is the most frequently occuring letter? Least frequently occuring?
print(word.value_counts().idxmax())
print(word.value_counts().idxmin())

#How many vowels are in the list?
vowels_in_word = (word.apply(number_of_vowels))
print(vowels_in_word.sum())

#How many consonants are in the list?
print(word.count() - vowels_in_word.sum())

#Create a series that has all of the same letters, but uppercased
upper_series = word.str.upper()
print(upper_series)

#Create a bar plot of the frequencies of the 6 most frequently occuring letters.
print(word.value_counts())
bar_values = word.value_counts()[0:7]
bar_values.plot.bar()





