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



"""