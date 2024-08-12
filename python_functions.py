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

"""
Nested Functions I

You've learned in the last video about nesting functions within functions. 
One reason why you'd like to do this is to avoid writing out the same computations within functions repeatedly. 
There's nothing new about defining nested functions: you simply define it as you would a regular function with def 
and embed it inside another function!

In this exercise, inside a function three_shouts(), you will define a nested function inner() that concatenates a string object with !!!. 
three_shouts() then returns a tuple of three elements, each a string concatenated with !!! using inner(). 

"""

# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))

############################################################################################

"""
Nested Functions II

One other pretty cool reason for nesting functions is the idea of a closure. 
This means that the nested or inner function remembers the state of its enclosing scope when called

In this exercise, you will complete the definition of the inner function inner_echo() and then call echo() a couple of times, 
each with a different argument.

Instructions
- Complete the function header of the inner function with the function name inner_echo() and a single parameter word1.
- Complete the function echo() so that it returns inner_echo.
- We have called echo(), passing 2 as an argument, and assigned the resulting function to twice. Your job is to call echo(), passing 3 as an argument. Assign the resulting function to thrice.
- Hit Submit to call twice() and thrice() and print the results.

"""

# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo

# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))

############################################################################################

"""
The keyword nonlocal and nested functions

In this exercise, you will use the keyword nonlocal within a nested function to alter the value of a variable defined in the enclosing scope.

Instructions
- Assign to echo_word the string word, concatenated with itself.
- Use the keyword nonlocal to alter the value of echo_word in the enclosing scope.
- Alter echo_word to echo_word concatenated with '!!!'.
- Call the function echo_shout(), passing it a single argument 'hello'.

"""

# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""
    
    # Concatenate word with itself: echo_word
    echo_word = word + word
    
    # Print echo_word
    print(echo_word)
    
    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""    
        # Use echo_word in nonlocal scope
        nonlocal echo_word
        
        # Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + '!!!'
    
    # Call function shout()
    shout()
    
    # Print echo_word
    print(echo_word)

# Call function echo_shout() with argument 'hello'
echo_shout('hello')

############################################################################################

"""
Functions with one default argument

Write a function that uses a default argument and then calling the function a couple of times.

Instructions
-   Complete the function header with the function name shout_echo.
    It accepts an argument word1 and a default argument echo with default value 1, in that order.
-   Use the * operator to concatenate echo copies of word1. Assign the result to echo_word.
-   Call shout_echo() with just the string, "Hey". Assign the result to no_echo.
-   Call shout_echo() with the string "Hey" and the value 5 for the default argument, echo. Assign the result to with_echo.

"""

# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo('Hey')

# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo('Hey', 5)

# Print no_echo and with_echo
print(no_echo)
print(with_echo)

############################################################################################

"""
Functions with multiple default arguments

You will now try your hand at defining a function with more than one default argument and then calling this function in various ways.

Instructions
-   Complete the function header with the function name shout_echo.
    It accepts an argument word1, a default argument echo with default value 1 and a default argument intense with default value False, in that order.
-   In the body of the if statement, make the string object echo_word upper case by applying the method .upper() on it.
-   Call shout_echo() with the string, "Hey", the value 5 for echo and the value True for intense. Assign the result to with_big_echo.
-   Call shout_echo() with the string "Hey" and the value True for intense. Assign the result to big_no_echo.

"""

# Define shout_echo
def shout_echo(word1, echo=1, intense=False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Make echo_word uppercase if intense is True
    if intense is True:
        # Make uppercase and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'

    # Return echo_word_new
    return echo_word_new

# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo('Hey',5,True)

# Call shout_echo() with "Hey" and intense=True: big_no_echo
big_no_echo = shout_echo('Hey',intense=True)

# Print values
print(with_big_echo)
print(big_no_echo)


############################################################################################

"""
Functions with variable-length arguments (*args)

Flexible arguments enable you to pass a variable number of arguments to a function. 
In this exercise, you will practice defining a function that accepts a variable number of string arguments.

The function you will define is gibberish() which can accept a variable number of string values. 
Its return value is a single string composed of all the string arguments concatenated together in the order they were passed to the function call. 
You will call the function with a single string argument and see how the output changes with another call using more than one string argument. 
Recall from the previous video that, within the function definition, args is a tuple.

"""

# Define gibberish
def gibberish(*args):
    """ Concatenate strings in *args together"""

    # Initialize an empty string: hodgepodge
    hodgepodge = ''

    # Concatenate the strings in args
    for word in args:
        hodgepodge += word

    return hodgepodge

# Call gibberish() with one string: one_word
one_word = gibberish('luke')

# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

# Print one_word and many_words
print(one_word)
print(many_words)

############################################################################################

"""
Functions with variable-length keyword arguments (**kwargs)

What makes **kwargs different is that it allows you to pass a variable number of keyword arguments to functions.

To understand this idea better, you're going to use **kwargs in this exercise to define a function that accepts a variable number of keyword arguments.
The function simulates a simple status report system that prints out the status of a character in a movie.

Instructions
- Complete the function header with the function name report_status. It accepts a single flexible argument **kwargs.
- Iterate over the key-value pairs of kwargs to print out the keys and values, separated by a colon ':'.
- In the first call to report_status(), pass the following keyword-value pairs: name="luke", affiliation="jedi" and status="missing".
- In the second call to report_status(), pass the following keyword-value pairs: name="anakin", affiliation="sith lord" and status="deceased".

"""

# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)

    print("\nEND REPORT")

# First call to report_status()
report_status(name='luke', affiliation='jedi', status='missing')

# Second call to report_status()
report_status(name='anakin', affiliation='sith lord', status='deceased')

############################################################################################

"""

"""


############################################################################################