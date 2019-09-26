# 1.) Use pandas to create a Series from the following data:
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
print(exam_scores.median())

#Plot a histogram of the scores.
plt.hist(exam_scores)

#Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.
def letter_grade_converter(grade):
        if grade >= 90:
            return ('A')
        elif grade >= 80:
            return ('B')
        elif grade >= 70:
            return('C')
        else:
            return('F')

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
plt.xlabel('Letters')
plt.ylabel('Frequency')
plt.show()






#______________________________________________________________________________________
from pydataset import data
#All the datasets loaded from the pydataset library will be pandas dataframes.

# 1.) Copy the code from the lesson to create a dataframe full of student grades.

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})



#Create a column named passing_english that indicates whether each student has a passing grade in reading.
df['passing_english'] = df.english >= 70

#Sort the english grades by the passing_english column. How are duplicates handled?
df.sort_values(by='passing_english') #Duplicates are sorted by index number.


#Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)
df.sort_values(['passing_english', 'name'], ascending=[True, True])

#Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.
df.sort_values(['passing_english', 'english'], ascending=[True, True])

#Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.
df['overall_grade'] = (df.math + df.reading + df.english) / 3









# 2.) Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
mpg = data('mpg')
#How many rows and columns are there?
mpg.shape

#What are the data types of each column?
mpg.dtypes

#Rename the cty column to city.
mpg.rename(columns={'cty':'city'}, inplace = True)

#Rename the hwy column to highway.
mpg.rename(columns={'hwy':'highway'}, inplace = True)

#Do any cars have better city mileage than highway mileage?
better_city = mpg[mpg.city > mpg.highway] #No cars have better city mileage than highway mileage
print(better_city)

#Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
mpg['mileage_difference'] = (mpg.highway - mpg.city)


#Which car (or cars) has the highest mileage difference?
mpg.sort_values('mileage_difference', ascending = False)

#Which compact class car has the lowest highway mileage? The best?
mpg.sort_values(['class', 'highway'], ascending = [True, False])
mpg.sort_values(['class', 'highway'], ascending = [True, True])

#Create a column named average_mileage that is the mean of the city and highway mileage.
mpg['average_mileage'] = (mpg.highway + mpg.city) /2

#Which dodge car has the best average mileage? The worst?
mpg.sort_values(['manufacturer', 'average_mileage'], ascending = [True, False])
mpg.sort_values(['manufacturer', 'average_mileage'], ascending = [True, True])








# 3.) Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
mammals = data('Mammals')
#How many rows and columns are there?
mammals.shape

#What are the data types?
mammals.dtypes

#Summarize the dataframe with .info and .describe
mammals.info
mammals.describe

#What is the the weight of the fastest animal?
fastest_animal = mammals.speed.idxmax()
print("The fastest animal is" , fastest_animal , "and its weight is ", mammals.weight[fastest_animal])

#What is the overal percentage of specials?
mammals.specials.value_counts(True)
special_mammals = mammals[mammals.specials == True]
print('The overall percentage of specials is', special_mammals.specials.count() / len(mammals) * 100)

#How many animals are hoppers that are above the median speed? What percentage is this?
total_hoppers = mammals.hoppers.sum()
median_speed = mammals.speed.median()
fast_animals = mammals[mammals.speed > median_speed]
fast_hoppers = fast_animals[mammals.hoppers == True]
fast_hoppers_count = fast_hoppers.hoppers.count()
print('There are',total_hoppers, 'total hoppers. The median speed of all animals is',median_speed,'. Of the total hoppers,',fast_hoppers_count,'are above the median speed.')
print('This is', (fast_hoppers_count/total_hoppers *100),'percent.')






