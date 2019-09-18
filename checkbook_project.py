#This is the welcome section. Here the user is welcomed and prompted for input.
#This section also opens the balance.txt file and keeps track of the current balance.

print("\nWelcome to your terminal checkbook!\n\nSelect one of the following options:\n\n1.) View current balance\n2.) Record a debit (withdrawal)\n3.) Record a credit (deposit)\n4.) Exit")
user_input = input("Enter your choice here:")
more_options = "\n\nWhat else would you like to do?\n\n1.) View current balance\n2.) Record a debit (withdrawal)\n3.) Record a credit (deposit)\n4.) Exit"
with open('balance.txt', 'r+') as b:
    bal = b.read()
current_balance = float(bal)

#This while loop will be prompted when a user enters an invalid entry. They will be prompted until they enter a valid entry.
while user_input not in "1234":
    print("Invalid entry.")
    user_input = input("\nTry again:")

#This while loop is the main section of the program. It is broken down into if/else statements that direct the user based on their input.
while user_input in "1234":

    #Checks and prints the current balance.
    if user_input == "1":
        print("\nYour balance is " + str(current_balance))
        print(more_options)
        user_input = input()
        while user_input not in "1234":
            print("Invalid entry.")
            user_input = input("\nTry again:")   

    #Records a debit, updates the current balance, and prompts the user for another input
    elif user_input == "2":
        with open("balance.txt", "w") as d:
            print("You have chosen to record a debit. Please enter the amount:")
            debit_user_input = input()
            d.write(debit_user_input)    
            debit_amount = float(debit_user_input)
            current_balance -= debit_amount
            print(more_options)
            user_input = input()
            while user_input not in "1234":
                print("Invalid entry.")
                user_input = input("\nTry again:") 

    #Records a credit, updates the current balance, and prompts the user for another input
    elif user_input == "3":
        with open("balance.txt", "w") as c:
            print("You have chosen to record a credit. Please enter the amount:")
            credit_user_input = input()
            c.write(credit_user_input)
            credit_amount = float(credit_user_input)
            current_balance += credit_amount
            print(more_options)
            user_input = input()
            while user_input not in "1234":
                print("Invalid entry.")
                user_input = input("\nTry again:") 

    #This section allows the user to exit the program. The current balance is updated one last time to the balance.txt file.    
    elif user_input == "4":
        with open("balance.txt", "w") as e:
            e.write(str(current_balance))
            print("\nHave a nice day!\nGoodbye!\n")
            break
    
