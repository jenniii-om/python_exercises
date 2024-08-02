"""
Write a basic list comprehension

The following list has been pre-loaded in the environment.
doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']

How would a list comprehension that produces a list of the first character of each string in doctor look like? 
Note that the list comprehension uses doc as the iterator variable. What will the output be?

"""

doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']

print([doc[0] for doc in doctor])

############################################################################################

"""
Writing list comprehensions

You now have all the knowledge necessary to begin writing list comprehensions!
Your job in this exercise is to write a list comprehension that produces a list of the squares of the numbers ranging from 0 to 9.

"""

# Create list comprehension: squares
squares = [i ** 2 for i in range(0,10)]

print(squares)

############################################################################################

"""
Nested list comprehensions

In this exercise, you will be writing a list comprehension within another list comprehension, or nested list comprehensions.

Let's step aside for a while from strings. 
One of the ways in which lists can be used are in representing multi-dimension objects such as matrices. 
Matrices can be represented as a list of lists in Python. For example a 5 x 5 matrix with values 0 to 4 in each row can be written as:

matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]

Your task is to recreate this matrix by using nested listed comprehensions.

"""

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0,5)] for i in range(0,5)]

# Print the matrix
for row in matrix:
    print(row)


############################################################################################

"""
Using conditionals in comprehensions(1)

An interesting mechanism in list comprehensions is that you can also create lists with values that meet only a certain condition. 
One way of doing this is by using conditionals on iterator variables.

You are given a list of strings fellowship and, using a list comprehension, 
you will create a list that only includes the members of fellowship that have 7 characters or more.


Instructions:
Use member as the iterator variable in the list comprehension.
For the conditional, use len() to evaluate the iterator variable. Note that you only want strings with 7 characters or more.

"""

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) >= 7]

# Print the new list
print(new_fellowship)


############################################################################################

"""
Using conditionals in comprehensions(2)

In this exercise, you will use an if-else statement on the output expression of the list.

You will work on the same list, fellowship and, 
using a list comprehension and an if-else conditional statement in the output expression, 
create a list that keeps members of fellowship with 7 or more characters and replaces others with an empty string. 
Use member as the iterator variable in the list comprehension.

"""

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member) >= 7 else '' for member in fellowship]

# Print the new list
print(new_fellowship)

############################################################################################

"""
Dict comprehensions

You will create a dictionary using the comprehension syntax for this exercise.
In this case, the comprehension is called a dict comprehension.

Recall that the main difference between a list comprehension and a dict comprehension is the use of curly braces {} instead of []. 
Additionally, members of the dictionary are created using a colon :, as in <key> : <value>.

You are given a list of strings fellowship and, using a dict comprehension, 
create a dictionary with the members of the list as the keys and the length of each string as the corresponding values.

"""

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}

# Print the new dictionary
print(new_fellowship)

############################################################################################

"""
Write your own generator expressions

Recall that generator expressions basically have the same syntax as list comprehensions, 
except that it uses parentheses () instead of brackets []

Now, you will start simple by creating a generator object that produces numeric values.

Instructions
-   Create a generator object that will produce values from 0 to 30. 
    Assign the result to result and use num as the iterator variable in the generator expression.
-   Print the first 5 values by using next() appropriately in print().
-   Print the rest of the values by using a for loop to iterate over the generator object.

"""

# Create generator object: result
result = (num for num in range(0,31))

# Print the first 5 values
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# Print the rest of the values
for value in result:
    print(value)

############################################################################################

"""
Changing the output in generator expressions

In this exercise, you will push this idea a little further by adding to the output expression of a generator expression. 
Because generator expressions and list comprehensions are so alike in syntax, this should be a familiar task for you!

You are given a list of strings lannister and, using a generator expression, 
create a generator object that you will iterate over to print its values.

Instructions
-   Write a generator expression that will generate the lengths of each string in lannister. 
    Use person as the iterator variable. Assign the result to lengths.
-   Supply the correct iterable in the for loop for printing the values in the generator object.

"""

# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
lengths = (len(person) for person in lannister)

# Iterate over and print the values in lengths
for value in lengths:
    print(value)

############################################################################################

"""
Build a generator

Generator functions are functions that, like generator expressions, yield a series of values,instead of returning a single value. 
A generator function is defined as you do a regular function, but whenever it generates a value, it uses the keyword yield instead of return.

In this exercise, you will create a generator function with a similar mechanism as the generator expression you defined in the previous exercise

Instructions
-   Complete the function header for the function get_lengths() that has a single parameter, input_list.
-   In the for loop in the function definition, yield the length of the strings in input_list.
-   Complete the iterable part of the for loop for printing the values generated by the get_lengths() generator function.
    Supply the call to get_lengths(), passing in the list lannister.

"""

# Create a list of strings
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string
    for person in input_list:
        yield len(person)

# Print the values generated by get_lengths()
for value in get_lengths(lannister):
    print(value)

############################################################################################

"""
List comprehension for time-stamped data

In this exercise, you will be using a list comprehension to extract the time from time-stamped Twitter data. 
The pandas package has been imported as pd and the file 'tweets.csv' has been imported as the df DataFrame for your use.

Instructions
-   Extract the column 'created_at' from df and assign the result to tweet_time.
    Fun fact: the extracted column in tweet_time here is a Series data structure!
-   Create a list comprehension that extracts the time from each row in tweet_time.
    Each row is a string that represents a timestamp, and you will access the 12th to 19th characters in the string to extract the time.
    Use entry as the iterator variable and assign the result to tweet_clock_time. Remember that Python uses 0-based indexing!

"""

import pandas as pd

df = pd.read_csv('csv_files/tweets.csv')

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time]

# Print the extracted times
print(tweet_clock_time)

############################################################################################

"""
Conditional list comprehensions for time-stamped data

Let's tweak your work further by adding a conditional that further specifies which entries to select.

In this exercise, you will be using a list comprehension to extract the time from time-stamped Twitter data. 
You will add a conditional expression to the list comprehension so that you only select the times in which entry[17:19] is equal to '19'.

Instructions
-   Extract the column 'created_at' from df and assign the result to tweet_time.
-   Create a list comprehension that extracts the time from each row in tweet_time. 
    Each row is a string that represents a timestamp, and you will access the 12th to 19th characters in the string to extract the time. 
    Use entry as the iterator variable and assign the result to tweet_clock_time. 
    Additionally, add a conditional expression that checks whether entry[17:19] is equal to '19'.

"""

df = pd.read_csv('csv_files/tweets.csv')

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']

# Print the extracted times
print(tweet_clock_time)
