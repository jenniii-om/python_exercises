year = [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061, 2062, 2063, 2064, 2065, 2066, 2067, 2068, 2069, 2070, 2071, 2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2099, 2100]
pop = [2.53, 2.57, 2.62, 2.67, 2.71, 2.76, 2.81, 2.86, 2.92, 2.97, 3.03, 3.08, 3.14, 3.2, 3.26, 3.33, 3.4, 3.47, 3.54, 3.62, 3.69, 3.77, 3.84, 3.92, 4.0, 4.07, 4.15, 4.22, 4.3, 4.37, 4.45, 4.53, 4.61, 4.69, 4.78, 4.86, 4.95, 5.05, 5.14, 5.23, 5.32, 5.41, 5.49, 5.58, 5.66, 5.74, 5.82, 5.9, 5.98, 6.05, 6.13, 6.2, 6.28, 6.36, 6.44, 6.51, 6.59, 6.67, 6.75, 6.83, 6.92, 7.0, 7.08, 7.16, 7.24, 7.32, 7.4, 7.48, 7.56, 7.64, 7.72, 7.79, 7.87, 7.94, 8.01, 8.08, 8.15, 8.22, 8.29, 8.36, 8.42, 8.49, 8.56, 8.62, 8.68, 8.74, 8.8, 8.86, 8.92, 8.98, 9.04, 9.09, 9.15, 9.2, 9.26, 9.31, 9.36, 9.41, 9.46, 9.5, 9.55, 9.6, 9.64, 9.68, 9.73, 9.77, 9.81, 9.85, 9.88, 9.92, 9.96, 9.99, 10.03, 10.06, 10.09, 10.13, 10.16, 10.19, 10.22, 10.25, 10.28, 10.31, 10.33, 10.36, 10.38, 10.41, 10.43, 10.46, 10.48, 10.5, 10.52, 10.55, 10.57, 10.59, 10.61, 10.63, 10.65, 10.66, 10.68, 10.7, 10.72, 10.73, 10.75, 10.77, 10.78, 10.79, 10.81, 10.82, 10.83, 10.84, 10.85]

print(year)
print(pop)

import numpy as np
import matplotlib.pyplot as plt

# plt.plot (year, pop)

# plt.show()


for i in range(100):
    print (i);



n = int(input("Enter value to get factorial of: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    print(factorial)



N = np.array(range(1, 100000+1))
print(N);


A = [int(A) for A in input("Array:").split(",")]
print("The array numbers are: ", A)


###

fruits = {'apple': 10, 'orange': 6, 'banana': 9}
fruits.items()

##

attendees_set = {"John Smith", "Alan Jones", "Roger Thompson",
                  "John Smith", "Brandon Sharp", "Sam Washington"}

type(attendees_set)

### FOR LOOP

# Create the tickets_sold variable
tickets_sold = 0

# Create the max_capacity variable
max_capacity = 30

# Loop through a range up to and including max_capacity's value
for tickets_sold in range(tickets_sold, max_capacity):
  
  # Add one to tickets_sold in each iteration
  tickets_sold += 1
  
print("Sold out:", tickets_sold, "tickets sold!")


###

courses = {"LLM Concepts": "AI", 
           "Introduction to Data Pipelines": "Data Engineering", 
           "AI Ethics": "AI",
           "Introduction to dbt": "Data Engineering", 
           "Writing Efficient Python Code": "Programming",
           "Introduction to Docker": "Programming"}

# Loop through the dictionary's keys and values
for key, value in courses.items():
  
  # Check if the value is "AI"
  if value == "AI":
    print(key, "is an AI course")
  
  # Check if the value is "Programming"
  elif value == "Programming":
    print(key, "is a Programming course")
  
  # Otherwise, print that it is a "Data Engineering" course
  else:
    print(key, "is a Data Engineering course")



### WHILE LOOP

tickets_sold = 0
max_capacity = 50

# Create a while loop
while tickets_sold < max_capacity:
  
  # Add one to tickets_sold in each iteration
  tickets_sold += 1

# Print the number of tickets sold
print("Sold out:", tickets_sold, "tickets sold!")



###

release_date = 26
current_date = 19

# Create a condition where current_date is less than or equal to the release_date
while current_date <= release_date:
  
  # Increment current_date by one
  current_date += 1
  
  # Promote purchases
  if current_date < 21:
    print("Purchase before the 21st for early access")
  
  # Check if the date is less than or equal to the 25th
  elif current_date <= 25:
    print("Coming soon!")
  else:
    print("Available now!")


###

# Appending to a list
#You've been provided with a dictionary called authors, which has information about 20 of the most popular fiction authors in the World. It contains the names of authors as keys and the number of books they've created as values.

#You're interested in finding out how many of these authors have made less than 25 books. To do this, you will create a list called authors_below_twenty_five, filling it with author names conditionally based on whether they have created less than 25 books.


authors = {'Penny Jordan': 200, 
           'Nicholas Sparks': 22, 
           'Ken Follett': 30, 
           'Erskine Caldwell': 25, 
           'Wilbur Smith': 32, 
           'Judith Krantz': 12, 
           'Harold Robbins': 23, 
           'J. K. Rowling': 22,
           'Debbie Macomber': 199,
           'Eiichiro Oda': 106,
           'Danielle Steel': 179, 
           'Barbara Cartland': 723, 
           'Georges Simenon': 570, 
           'Corín Tellado': 4000, 
           'Clive Cussler': 37, 
           'Sidney Sheldon': 21, 
           'Dean Koontz': 91, 
           'Janet Dailey': 93, 
           'Jirō Akagawa': 500, 
           'Stephen King': 77
           }

# Create an empty list
authors_below_twenty_five = []

# Loop through the authors dictionary
for key, value in authors.items():
  
  # Check for values less than 25
  if value < 25:
    
    # Append the author to the list
    authors_below_twenty_five.append(key)
    
print(authors_below_twenty_five)


###

genre_sales = {'Adventure': 367500000,
               'Horror': 312500000, 
               'Literature': 80000000,
               'Manga': 5166000000,
               'Mystery': 300000000,
               'Romance': 252500000,
               'Thriller': 320000000
               }

for genre, average_sale in genre_sales.items():
    
    # Filter for the maximum sales value
    if average_sale == 5166000000:
      
      # Print the genre
      print("Most popular genre: ", genre)
      print("Average sales: ", average_sale)
    
    # Filter for the minimum sales value
    elif average_sale == 80000000:
      
      # Print the genre
      print("Least popular genre: ", genre)
      print("Average sales: ", average_sale)

###

course_ratings = {"LLM Concepts": 4.7, 
                  "Introduction to Data Pipelines": 4.75, 
                  "AI Ethics": 4.62, 
                  "Introduction to dbt": 4.81}

# Print the number of key-value pairs
num_courses = len(course_ratings)
print(num_courses)


###

# Create the clean_string function
def clean_string(text):
  
  # Replace spaces with underscores
  no_spaces = text.replace(" ", "_")
  
  # Convert to lowercase
  clean_text = no_spaces.lower()
  
  # Display the final text as an output
  return clean_text

converted_text = clean_string("I LoVe dATaCamP!")
print(converted_text)


###

# Data structure converter function

# Create the convert_data_structure function
def convert_data_structure(data, data_type="list"):
  
  # If data_type is "tuple"
  if data_type == "tuple":
    data = tuple(data)
  
  # Else if data_type is set, convert to a set
  elif data_type == "set":
    data = set(data)
  else:
    data = list(data)
  return data

# Call the function to convert to a set
convert_data_structure({"a", 1, "b", 2, "c", 3}, data_type="set")


###

def clean_string(text):
  
  # Add a single-line docstring
  """Swap spaces to underscores and convert text to lowercase"""  
  
  no_spaces = text.replace(" ", "_")
  clean_text = no_spaces.lower()
  return clean_text

# Access the docstring
print(clean_string.__doc__)


###

# Create the convert_data_type function
def convert_data_structure(data, data_type="list"):
  # Add a multi-line docstring
  """
  Convert a data structure to a list, tuple, or set.
  
  Args:
  	data (list, tuple, or set): A data structure to be converted.
    data_type (str): String representing the type of structure to convert data to.
    
  Returns:
  	data (list, tuple, or set): Converted data structure.
  """
  if data_type == "tuple":
    data = tuple(data)
  elif data_type == "set":
    data = set(data)
  else:
    data = list(data)
  return data

print(help(convert_data_structure))


####

# arbitrary arguments

# Define a function called concat
def concat(*args):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python args tuple
  for arg in args:
    result += " " + arg
  return result

# Call the function
print(concat("Python", "is", "great!"))


###

# arbitrary keyword arguments

# Define a function called concat
def concat(**kwargs):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python kwargs
  for kwarg in kwargs.values():
    result += " " + kwarg
  return result

# Call the function
print(concat(start="Python", middle="is", end="great!"))

###

# lambda function - adding tax

sale_price = 29.99

# Define a lambda function called add_tax
add_tax = lambda x: x*1.2

# Call the lambda function
print(add_tax(sale_price))


###

sale_price = 29.99

# Call a lambda function adding 20% to sale_price
print((lambda x: x * 1.2)(sale_price))


###


sales_prices = [29.99, 9.95, 14.50, 39.75, 60.00]

# Create add_taxes to add 20% to each item in sales_prices
add_taxes = map(lambda x: x * 1.2, sales_prices)

# Use add_taxes to return a new list with updated values
print(list(add_taxes))



####

# Avoiding errors - try-excet

def snake_case(text):
  # Attempt to clean the text
  try:
    # Swap spaces for underscores
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
    print(clean_text)
  # Run this code if an error occurs
  except:
    print("The snake_case() function expects a string as an argument, please check the data type provided.")
    
snake_case("User Name 187")
snake_case(1)


# returning errors

def snake_case(text):
  # Check the data type
  if type(text) == str :
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
  else:
    # Return a TypeError error if the wrong data type was used
    raise TypeError("The snake_case() function expects a string as an argument, please check the data type provided.")
    
snake_case("User Name 187")

###
