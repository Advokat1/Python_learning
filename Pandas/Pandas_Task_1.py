"""
Задание №1
In the cell below, create a DataFrame fruits that looks like this:
    Apples  Bananas
0   30      21
"""
# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.
fruits = pd.DataFrame({'Apples': [30], 'Bananas': [21]})

# Check your answer
q1.check()
fruits

"""
Задание №2
Create a dataframe fruit_sales that matches the diagram below:`
        Apples      Bananas
2017 Sales    35    21
2018 Sales    41    34        
"""

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruit_sales.
fruit_sales = pd.DataFrame({'Apples':[35, 41], 'Bananas':[21, 34]}, index = ['2017 Sales', '2018 Sales'])

# Check your answer
q2.check()
fruit_sales

"""
Задание №3
Create a variable ingredients with a Series that looks like:
Flour     4 cups
Milk       1 cup
Eggs     2 large
Spam       1 can
Name: Dinner, dtype: object       
"""
ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name = 'Dinner')

# Check your answer
q3.check()
ingredients

"""
Задание №4
Read the following csv dataset of wine reviews into a DataFrame called reviews:       
"""

reviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv", index_col=0)

# Check your answer
q4.check()
reviews

"""
Задание №5
Run the cell below to create and display a DataFrame called animals:      
"""
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals

"""
        Cows    Goats
Year 1  12      22
Year 2  20      19

In the cell below, write code to save this DataFrame to disk as a csv file with the name cows_and_goats.csv.
"""

# Your code goes here
animals.to_csv(r'cows_and_goats.csv')
# Check your answer
q5.check()
