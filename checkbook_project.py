print("\nWelcome to your terminal checkbook!\n\nSelect one of the following options:\n\n1.) View current balance\n2.) Record a debit (withdrawal)\n3.) Record a credit (deposit)\n4.) Exit")
user_input = input("Enter your choice here:")
more_options = "\n\nWhat else would you like to do?\n\n1.) View current balance\n2.) Record a debit (withdrawal)\n3.) Record a credit (deposit)\n4.) Exit"
with open('balance.txt', 'r+') as b:
    bal = b.read()
current_balance = float(bal)

while user_input not in "1234":
    print("Invalid entry.")
    user_input = input("\nTry again:")

while user_input in "1234":
    if user_input == "1":
        print("\nYour balance is " + str(current_balance))
        print(more_options)
        user_input = input()   

    elif user_input == "2":
        with open("balance.txt", "w") as d:
            print("You have chosen to record a debit. Please enter the amount:")
            debit_user_input = input()
            d.write(debit_user_input)
            debit_amount = float(debit_user_input)
            current_balance -= debit_amount
            print(more_options)
            user_input = input()

    elif user_input == "3":
        with open("balance.txt", "w") as c:
            print("You have chosen to record a credit. Please enter the amount:")
            credit_user_input = input()
            c.write(credit_user_input)
            credit_amount = float(credit_user_input)
            current_balance += credit_amount
            print(more_options)
            user_input = input()
        
    elif user_input == "4":
        with open("balance.txt", "w") as e:
            e.write(str(current_balance))
            print("Goodbye!\n")
            break

