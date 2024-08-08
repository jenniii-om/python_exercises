"""
Write a simple function

Define a function, shout(), which simply prints out a string with three exclamation marks '!!!' at the end.

"""

# Define the function shout
def shout():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = 'congratulations' + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout
shout()

############################################################################################

"""
Single parameter functions

You will now update shout() by adding a parameter so that it can accept and process any string argument passed to it.

"""

# Define shout with the parameter, word
def shout(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout with the string 'congratulations'
shout('congratulations')

############################################################################################

"""
Functions that return single values

"""

# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Replace print with return
    return(shout_word)

# Pass 'congratulations' to shout: yell
yell = shout('congratulations')

# Print yell
print(yell)

############################################################################################

"""
Functions with multiple parameters

You are now going to use what you've learned to modify the shout() function further. Here, you will modify shout() to accept two arguments. 

"""

# Define shout with parameters word1 and word2
def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'

    # Concatenate word 2 with '!!!': shout2
    shout2 = word2 + '!!!'

    # Concatenate shout1 and shout2: new_shout
    new_shout = shout1 + shout2

    # Return new_shout
    return new_shout

# Pass 'congratulations' and 'you' to shout(): yell
yell = shout('congratulations', 'you')

# Print yell
print(yell)

############################################################################################

"""
A brief introduction to tuples

"""

nums = (3,4,6)
print(type(nums))

num1, num2, num3 = nums
even_nums = (2, num2, num3)
print(even_nums)

############################################################################################

"""
Functions that return multiple values

Using a tuple (unpack)
"""

# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)

    # Return shout_words
    return shout_words

# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = shout_all('congratulations', 'you')

# Print yell1 and yell2
print(yell1)
print(yell2)

############################################################################################

"""
Bringing it all together (1)

You will load a dataset and develop functionalities to extract simple insights from the data.

For this exercise, your goal is to recall how to load a dataset into a DataFrame. 
The dataset contains Twitter data and you will iterate over entries in a column to build a dictionary in which 
the keys are the names of languages and the values are the number of tweets in the given language. 

"""

# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
df = pd.read_csv('csv_files/tweets.csv')

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df['lang']

# Iterate over lang column in DataFrame
for entry in col:

    # If the language is in langs_count, add 1 
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1

# Print the populated dictionary
print(langs_count)

############################################################################################

"""
Bringing it all together (2)

In this exercise, you will define a function with the functionality you developed in the previous exercise, 
return the resulting dictionary from within the function, and call the function with the appropriate arguments.

"""

tweets_df = pd.read_csv('csv_files/tweets.csv')

tweets_df.head()

# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Return the langs_count dictionary
    return langs_count

# Call count_entries(): result
result = count_entries(tweets_df, 'lang')

# Print the result
print(result)

############################################################################################

"""
The keyword global

In this exercise, you will use the keyword global within a function to alter the value of a variable defined in the global scope.

Instructions
- Use the keyword global to alter the object team in the global scope.
- Change the value of team in the global scope to the string "justice league". Assign the result to team.
- Hit the Submit button to see how executing your newly defined function change_team() changes the value of the name team!

"""

# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    global team

    # Change the value of team in global: team
    team = "justice league"
    
# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)

############################################################################################