"""
Задание 1
Select the description column from reviews and assign the result to the variable desc.
"""
# Your code here
desc = reviews.description

# Check your answer
q1.check()

#Follow-up question: what type of object is desc? If you're not sure, you can check by calling Python's type function: type(desc).
#I think, it`s Series

"""
Задание 2
Select the first value from the description column of reviews, assigning it to variable first_description.
"""
first_description = reviews.description[0]

# Check your answer
q2.check()
first_description


"""
Задание 3
Select the first row of data (the first record) from reviews, assigning it to the variable first_row.
"""
first_row = reviews.iloc[0]

# Check your answer
q3.check()
first_row

"""
Задание 4
Select the first 10 values from the description column in reviews, assigning the result to variable first_descriptions.
Hint: format your output as a pandas Series.
"""
first_descriptions = reviews.description.iloc[:10]

# Check your answer
q4.check()
first_descriptions

"""
Задание 5
Select the records with index labels 1, 2, 3, 5, and 8, assigning the result to the variable sample_reviews.
In other words, generate the following DataFrame:
"""
sample_reviews = reviews.iloc[[1, 2, 3, 5, 8]]

# Check your answer
q5.check()
sample_reviews

"""
Задание 6
Create a variable df containing the country, province, region_1, and region_2 
columns of the records with the index labels 0, 1, 10, and 100. In other words, generate the following DataFrame:
"""
df = reviews.loc[[0, 1, 10, 100], ['country', 'province', 'region_1', 'region_2']]

# Check your answer
q6.check()
df

"""
Задание 7
Create a variable df containing the country and variety columns of the first 100 records.
Hint: you may use loc or iloc. When working on the answer this question and the several of the ones that follow, keep the following "gotcha" described in the tutorial.
"""
df = reviews.loc[:99, ['country', 'variety']]

# Check your answer
q7.check()
df

"""
Задание 8
Create a DataFrame italian_wines containing reviews of wines made in Italy. Hint: reviews.country equals what?
"""
italian_wines = reviews.loc[reviews.country == 'Italy']

# Check your answer
q8.check()

"""
Задание 9
Create a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand.
"""
top_oceania_wines = reviews.loc[((reviews.country == 'Australia') & (reviews.points >= 95))|((reviews.country == 'New Zealand') & (reviews.points >= 95))]

# Check your answer
q9.check()
top_oceania_wines
