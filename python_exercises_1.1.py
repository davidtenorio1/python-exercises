#You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?
cost = 3 * (1 + 3 + 5)
#Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
g_rate = 400, f_rate = 350, a_rate = 380
g_hours = 6, f_hours = 10, a_hours = 4
payment = g_rate * g_hours + a_rate * a_hours + f_rate * f_hours
print(payment)
#A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
class_has_space = True
schedule_works = False
enrollment_egilibility = class_has_space and schedule_works
#A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
is_premium_member = True
offer_not_expired = True
customer_purchased_more_than_two_items = True
product_offer_applicability = offer_not_expired and (customer_purchased_more_than_two_items or is_premium_member)


#Use the following code to follow the instructions below:
#username = 'codeup'
#password = 'notastrongpassword'
#Create a variable that holds a boolean value for each of the following conditions:
#the password must be at least 5 characters
#the username must be no more than 20 characters
#the password must not be the same as the username
#bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'

password_at_least_five_characters = len(password) >= 5
username_no_more_than_twenty_characters = len(username) <= 20
password_and_username_different = username != password

username_starts_or_ends_with_white_space = username[0] == " " or username[-1] == " "
password_starts_or_ends_with_white_space = password[0] == " " or password[-1] == " "

bonus = username_starts_or_ends_with_white_space or password_starts_or_ends_with_white_space