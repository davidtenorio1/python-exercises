import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pydataset import data
from env import host, user, password

# Use the iris database to answer the following quesitons:

iris = sns.load_dataset('iris')

# What does the distribution of petal lengths look like?
sns.distplot(iris.petal_length)
sns.boxplot(data=iris.petal_length)

# Is there a correlation between petal length and petal width?
sns.relplot(data=iris, x='petal_length', y='petal_width')
#Yes
# Would it be reasonable to predict species based on sepal width and sepal length?
sns.relplot(data=iris, x='sepal_length', y='sepal_width', hue = 'species')
#Yes, but it would be not be entirely accurate
# Which features would be best used to predict species?
sns.relplot(data=iris, x='petal_length', y='petal_width', hue = 'species')
sns.relplot(data=iris, x='sepal_length', y='sepal_width', hue = 'species')
sns.pairplot(data = iris, hue = 'species')



# Using the lesson as an example, use seaborn's load_dataset function to load the anscombe data set. 
# Use pandas to group the data by the dataset column, and calculate summary statistics for each dataset. 
# What do you notice?
anscombe = sns.load_dataset('anscombe')
df = pd.DataFrame(anscombe)
group_datasets = df.groupby('dataset').describe()

# Plot the x and y values from the anscombe data. 
# Each dataset should be in a separate column.
sns.relplot(data = anscombe, x = 'x', y = 'y', col = 'dataset')

# Load the InsectSprays dataset and read it's documentation. 
# Create a boxplot that shows the effectiveness of the different insect sprays.
data('InsectSprays', True)
insect_sprays = data('InsectSprays')
sns.boxplot(data=insect_sprays, x = 'spray', y = 'count')

# Load the swiss dataset and read it's documentation. 
# Create visualizations to answer the following questions:
swiss = data('swiss')
data('swiss', True)
swiss_df = pd.DataFrame(swiss)

# Create an attribute named is_catholic that holds a boolean value of whether or not the province is Catholic. 
# (Choose a cutoff point for what constitutes catholic)
swiss_df['is_catholic'] = swiss_df.Catholic >= 50

# Does whether or not a province is Catholic influence fertility?
# Yes
sns.boxplot(data = swiss_df, x = 'is_catholic', y = 'Fertility' )

# What measure correlates most strongly with fertility?
swiss.corr().Fertility
sns.heatmap(data=swiss.corr(), cmap = 'GnBu')

# Using the chipotle dataset from the previous exercise, create a bar chart that shows the 4 most popular items and the revenue produced by each.
def get_db_url(user, password, host, database_name):
    url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
    return url
chipotle_url = get_db_url(user,password,host,'chipotle')
query = 'SELECT * FROM orders'
orders = pd.read_sql(query, chipotle_url)
orders.head()
orders.item_price = orders.item_price.str.replace('$', '').astype('float')
four_most_popular = (orders.groupby('item_name')
 .sum()
 .drop(columns='order_id')
 .rename(columns={'quantity': 'units_sold', 'item_price': 'revenue'})
 .sort_values(by='units_sold', ascending=False)
 .head(4)
 .reset_index()
)

sns.barplot(data=four_most_popular, y='revenue', x='item_name')
plt.ylabel('')
plt.xticks()



# Load the sleepstudy data and read it's documentation. 
# Use seaborn to create a line chart of all the individual subject's reaction times and a more prominant line showing the average change in reaction time.
sleep = data('sleepstudy')
sleep.Subject = 'subject_' + sleep.Subject.astype(str)
sns.lineplot(data=sleep, y='Reaction', x='Days', hue='Subject', alpha=.4)
sns.lineplot(data=sleep, y='Reaction', x='Days', color='navy')





