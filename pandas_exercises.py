import pandas as pd
import numpy as np
from pydataset import data
from env import host, user, password

# 1.) Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:
mpg = data('mpg')

# On average, which manufacturer has the best miles per gallon?
mpg['average_mpg'] = (mpg.cty + mpg.hwy)/2
manufacturer_mpg = mpg.groupby('manufacturer').average_mpg.mean()
manufacturer_mpg.idxmax()

# How many different manufacturers are there?
len(manufacturer_mpg)

# How many different models are there?
unique_models = len(mpg.model.unique())


# Do automatic or manual cars have better miles per gallon?
mpg['is_auto'] = mpg.trans.str.contains('auto')
transmission_mpg = mpg.groupby('is_auto').average_mpg.mean()





# 2.) Joining and Merging
#Copy the users and roles dataframes from the examples above. 
users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles
# What do you think a right join would look like? An outer join? 
pd.merge(
    users.rename(columns={'id': 'user_id', 'name': 'username'}),
    roles.rename(columns={'name': 'role_name'}),
    left_on='role_id', right_on='id', how='left')
# What happens if you drop the foreign keys from the dataframes and try to merge them?










# 3.) Getting data from SQL databases
# Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url formatted like in the examples in this lesson.
def get_db_url(user, password, host, database_name):
    url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
    return url

# Use your function to obtain a connection to the employees database.
employees_url = get_db_url(user,password,host,'employees')

# Once you have successfully run a query:
pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', employees_url)

#Intentionally make a typo in the database url. What kind of error message do you see?
#pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', employees_url)
#NameError: name 'getdb_url is not defined

# Intentionally make an error in your SQL query. What does the error message look like?
#pd.read_sql('SELECT * FROM employes LIMIT 5 OFFSET 50', employees_url)
#ProgrammingError: table employees.employes doesn't exist
#pd.read_sql('SELCT * FROM employees LIMIT 5 OFFSET 50', employees_url)
#ProgrammingError: You have an error in your SQL syntax

# Read the employees and titles tables into two separate dataframes
employees = pd.read_sql('SELECT * FROM employees', employees_url)
titles = pd.read_sql('SELECT * FROM titles', employees_url)

# Visualize the number of employees with each title.
current_titles = pd.read_sql('SELECT title, count(title) as number_of_employees FROM titles WHERE to_date = "9999-01-01" group by title', employees_url)


# Join the employees and titles dataframes together.
employees_titles = pd.merge(employees, titles)

# Visualize how frequently employees change titles.


# For each title, find the hire date of the employee that was hired most recently with that title.
titles_by_hire_date = pd.read_sql('SELECT * from employees join titles on employees.emp_no = titles.emp_no order by title, hire_date desc', employees_url)
s = titles_by_hire_date.groupby('title').head(1)

# Write the code necessary to create a cross tabulation of the number of titles by department. (Hint: this will involve a combination of SQL and python/pandas code)
joined_tables = pd.read_sql('SELECT * from employees join titles on employees.emp_no = titles.emp_no and to_date = "9999-01-01" join dept_emp on dept_emp.emp_no = titles.emp_no join departments on departments.dept_no = dept_emp.dept_no order by title', employees_url)
titles_by_department = pd.crosstab(joined_tables.title, joined_tables.dept_name)







# 4.) Use your get_db_url function to help you explore the data from the chipotle database. Use the data to answer the following questions:
chipotle_url = get_db_url(user,password,host,'chipotle')

# What is the total price for each order?
orders = pd.read_sql('SELECT * FROM orders', chipotle_url)
orders['clean_price'] = orders.item_price.str.replace('$','').astype(float)
total_price_per_order = orders.groupby('order_id').sum()

# What are the most popular 3 items?
popular_items = pd.read_sql('select item_name, count(item_name) from orders group by item_name order by count(item_name) desc limit 3', chipotle_url)

# Which item has produced the most revenue?
item_prices = pd.read_sql('select item_name, item_price from orders order by item_name', chipotle_url)
item_prices['clean_item_prices'] = item_prices.item_price.str.replace('$','').astype(float)
most_revenue = item_prices.groupby('item_name').sum()
most_revenue.sort_values(by=['clean_item_prices'], ascending = False).head(1)






 


