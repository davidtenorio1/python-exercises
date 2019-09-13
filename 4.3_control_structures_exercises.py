#1. Conditional Basics
#prompt the user for a day of the week, print out whether the day is Monday or not
#prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day_of_the_week = input( "Choose a day of the week:")
if day_of_the_week == "Monday":
    print("You chose Monday")
else:
    print("You did not choose Monday")

day_of_the_week_two = input( "Choose a day of the week:")

if (day_of_the_week_two) in ["Monday",'Tuesday','Wednesday','Thursday','Friday']:
    print("You chose a day during the week")
else:
    print("You chose a day on the weekend")

#create variables and make up values for
#the number of hours worked in one week
#the hourly rate
#how much the week's paycheck will be
#write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

number_of_weekly_work_hours = 80
hourly_rate = 20
weekly_paycheck = hourly_rate * number_of_weekly_work_hours

if number_of_weekly_work_hours <= 40:
    weekly_paycheck = hourly_rate * number_of_weekly_work_hours

elif number_of_weekly_work_hours >40:
    weekly_paycheck = (hourly_rate * 40) + 1.5 * hourly_rate * (number_of_weekly_work_hours - 40)

print(weekly_paycheck)

#2. Loop Basics
#a. While
#Create an integer variable i with a value of 5.
#Create a while loop that runs so long as i is less than or equal to 15
#Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1

#Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i <=100:
    print(i)
    i+= 2
#Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >=-10:
    print(i)
    i-=5
#Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
i = 2
while i <=1000000:
    print(i)
    i = i**2

#Write a loop that uses print to create the output shown below.
i = 100
while i >0:
    print(i)
    i -= 5

#For Loops
#Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
user_number = input("Select a natrual number :")
user_number_int = int(user_number)
i = 1
for i in range(1,11):
    print(user_number, " x ", i, "=", user_number_int*i)
    i+=1

#Create a for loop that uses print to create the output shown below.
#1
#22
#333
#4444
#55555
#666666
#7777777
#88888888
#999999999
i = 1
for i in range(1,10):
    print(str(i)*i)

#Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
user_prompt = input("Input an odd natural number between 1 and 50:")
while (user_prompt.isdigit()) == False:
    print("Invalid input.Try again:")
    user_prompt = input()
    if user_prompt.isdigit() == True:
        break

print("Number to skip is ", user_prompt)
for i in range(1,50):
    print("Here is an odd number: ", i)
    i+=2

#The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)
user_prompt = input("Enter a positive number:")
while (user_prompt.isdigit()) == False:
    print("Invalid input.Try again:")
    user_prompt = input()
    if user_prompt.isdigit() == True:
        break
user_number = int(user_prompt)
i=0
while i <= user_number:
    print(i)
    i += 1

#Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.
user_prompt = input("Enter a positive number:")
while (user_prompt.isdigit()) == False:
    print("Invalid input.Try again:")
    user_prompt = input()
    if user_prompt.isdigit() == True:
        break
user_number = int(user_prompt)
i=user_number
while i >= 1:
    print(i)
    i -= 1

#3. Fizzbuzz
#One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
#Write a program that prints the numbers from 1 to 100.
i = 1
while i <= 100:
    print(i)
    i+=1

#For multiples of three print "Fizz" instead of the number
i = 1
while i <= 100:
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)
    i+=1

#For the multiples of five print "Buzz".
i = 1
while i <= 100:
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i+=1

#For numbers which are multiples of both three and five print "FizzBuzz".
i = 1
while i <= 100:
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i+=1

#4. Display a table of powers.
#Prompt the user to enter an integer.
#Display a table of squares and cubes from 1 to the value entered.
#Ask if the user wants to continue.
#Assume that the user will enter valid data.
#Only continue if the user agrees to.

user_input = input("What number would you like to go up to?")
user_number_int = int(user_input)
i=1
while i <= user_number_int:
    print(i, i**2, i**3)
    i+=1

#E5.
""" Convert given number grades into letter grades.
Prompt the user for a numerical grade from 0 to 100.
Display the corresponding letter grade.
Prompt the user to continue.
Assume that the user will enter valid integers for the grades.
The application should only continue if the user agrees to.
Grade Ranges:
A : 100 - 88
B : 87 - 80
C : 79 - 67
D : 66 - 60
F : 59 - 0
Bonus
Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+). """
while True:
    num_grade=input("Please enter a grade between 0 and 100")
    num_grade=int(num_grade)
    if num_grade>=88:
        print('A')
    elif num_grade>=80:
        print('B')
    elif num_grade>=67:
        print('C')
    elif num_grade>=60:
        print('D') 
    else:
        print('F')
    prompt_user_continue=input("Would you like to continue? Y/N") 
    if prompt_user_continue.upper()=="N":
        break

#6
""" Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre. """

book_list=[{'title':"Lamb",'author':"Christopher Moore",'genre':"fiction"},
{'title':"The Lean Startup",'author':"Eric Ries",'genre':"business"},{'title':"Devil in a White City",'author':"Eric Larson",'genre':"True Crime"},{'title':"Tom Sawyer",'author':"Mark Twain",'genre':"fiction"}]
for book in book_list:
    print("The book title is: "+book['title'])
    print("The book author is: "+book['author'])
    print("The book genre is: "+book['genre'])


#Exercise 6.a
genre_filter=input("Please enter a genre")
for book in book_list:
    if book['genre']==genre_filter:
        print("The book title is: "+book['title'])
        print("The book author is: "+book['author'])







