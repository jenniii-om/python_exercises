"""
You are provided with a list of strings flash. 
You will practice iterating over the list by using a for loop. 
You will also create an iterator for the list and access the values from the iterator.
"""

# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for person in flash:
    print(person)

# Create an iterator for flash: superhero
superhero = iter(flash)

# Print each item from the iterator
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))



############################################################################################

"""
Iterating over iterables (2)
One of the things you learned about in this chapter is that not all iterables are actual lists. 
A couple of examples that we looked at are strings and the use of the range() function. 
In this exercise, we will focus on the range() function.

You can use range() in a for loop as if it's a list to be iterated over:
for i in range(5):
    print(i)
"""

# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# Loop over range(3) and print the values
for num in range(3):
    print(num)


# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))


############################################################################################

"""
Iterators as function arguments

You've been using the iter() function to get an iterator object, 
as well as the next() function to retrieve the values one by one from the iterator object.

There are also functions that take iterators and iterables as arguments. 
For example, the list() and sum() functions return a list and the sum of elements, respectively.

In this exercise, you will use these functions by passing an iterable from range() and then printing the results of the function calls.

"""

# Create a range object: values
values = range(10,21)

# Print the range object
print(values)

# Create a list of integers: values_list
values_list = list(values)

# Print values_list
print(values_list)

# Get the sum of values: values_sum
values_sum = sum(values_list)

# Print values_sum
print(values_sum)


