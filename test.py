print("I will help you calculate the tip amount")
total_input = input("What is the bill total?")
total_in_dollars = float(total_input)
tip_input = input("What percent tip would you like to leave? (a number between 0 and 1)")
tip_percentage = float(tip_input)

def calculate_tip_amount (x,y):
    return x * y
print(calculate_tip_amount(total_in_dollars,tip_percentage))