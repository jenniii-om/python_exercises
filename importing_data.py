"""
Importing entire text files

In this exercise, you'll be working with the file moby_dick.txt. 
It is a text file that contains the opening sentences of Moby Dick, one of the great American novels! 
In the video, you've seen you could open such a file using file = open('moby_dick.txt', mode='r'). 
You could then read from it with file.read() and close the file using file.close(). 
However, using context managers allows you to do this more effectively. 

In this exercise, you will gain experience opening a text file, printing its contents and, finally, closing it by using a context manager.

"""

# Open a file as read-only and bind it to file
with open('files/moby_dick.txt', mode='r') as file:
  	# Print it
    print(file.read())

############################################################################################

"""
Importing text file line by line

For large files, we may not want to print all of their content to the shell: you may wish to print only the first few lines. 
Enter the readline() method, which allows you to do this. 
When a file called file is open, you can print out the first line by executing file.readline(). 
If you execute the same command again, the second line will print, and so on.

"""

# Read & print the first 3 lines
with open('files/moby_dick.txt', 'r') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

############################################################################################

"""
Using NumPy to import flat files

In this exercise, you're now going to load the MNIST digit recognition dataset using the numpy function loadtxt() and see just how easy it can be:
The first argument will be the filename.
The second will be the delimiter which, in this case, is a comma.

Instructions
- Fill in the arguments of np.loadtxt() by passing file and a comma ',' for the delimiter.
- Fill in the argument of print() to print the type of the object digits. Use the function type().
- Execute the rest of the code to visualize one of the rows of the data.
"""

# Import packages
import numpy as np
import matplotlib.pyplot as plt

# Assign filename to variable: file
file = 'csv_files/mnist_kaggle_some_rows.csv'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')

# Print datatype of digits
print(type(digits))

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

############################################################################################

"""
Importing different datatypes

The file seaslug.txt has a text header, consisting of strings is tab-delimited.
This data consists of the percentage of sea slug larvae that had metamorphosed in a given time period. Read more here (http://www.stat.ucla.edu/~rgould/datasets/aboutseaslugs.html)

Due to the header, if you tried to import it as-is using np.loadtxt(), Python would throw you a ValueError and tell you that it could not convert string to float. 
There are two ways to deal with this: firstly, you can set the data type argument dtype equal to str (for string).
Alternatively, you can skip the first row as we have seen before, using the skiprows argument.

Instructions
- Complete the first call to np.loadtxt() by passing file as the first argument.
- Execute print(data[0]) to print the first element of data.
- Complete the second call to np.loadtxt(). The file you're importing is tab-delimited, the datatype is float, and you want to skip the first row.
- Print the 10th element of data_float by completing the print() command. Be guided by the previous print() call.
-Execute the rest of the code to visualize the data.

"""

# Assign filename: file
file = 'files/seaslug.txt'

# Import file: data
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 10th element of data_float
print(data_float[9])

# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()

############################################################################################

"""
Using pandas to import flat files as DataFrames(1)

"""

import pandas as pd

file = 'csv_files/titanic_sub.csv'
df = pd.read_csv(file)

df.head()

############################################################################################

"""
Using pandas to import flat files as DataFrames(2)

In the last exercise, you were able to import flat files into a pandas DataFrame. 
As a bonus, it is then straightforward to retrieve the corresponding numpy array using the method .to_numpy(). 
You'll now have a chance to do this using the MNIST dataset.

Instructions
-Import the first 5 rows of the file into a DataFrame using the function pd.read_csv() and assign the result to data.
 You'll need to use the arguments nrows and header (there is no header in this file).
-Build a numpy array from the resulting DataFrame in data and assign to data_array.
-Execute print(type(data_array)) to print the datatype of data_array.

"""
import pandas as pd

file = 'csv_files/mnist_kaggle_some_rows.csv'

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file, nrows=5, header=None)

# Build a numpy array from the DataFrame: data_array
data_array = data.to_numpy()

# Print the datatype of data_array to the shell
print(type(data_array))

############################################################################################

"""
Customizing you pandas import

The pandas package is great at dealing with many of the issues you will encounter when importing data as a data scientist, 
such as comments occurring in flat files, empty lines and missing values (NA or NaN). 
To wrap up this chapter, you're going to import a corrupted copy of the Titanic dataset titanic_corrupt.txt, which contains comments after the character '#', and is tab-delimited.

Instructions
-   Complete the sep (the pandas version of delimiter), comment and na_values arguments of pd.read_csv(). 
    comment takes characters that comments occur after in the file, which in this case is '#'. 
    na_values takes a list of strings to recognize as NA/NaN, in this case the string 'Nothing'.
-   Execute the rest of the code to print the head of the resulting DataFrame and plot the histogram of the 'Age' of passengers aboard the Titanic.

"""

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Assign filename: file
file = 'csv_files/titanic_sub.csv'

# Import file: data
data = pd.read_csv(file, sep=',', comment='#', na_values='Nothing')

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()

############################################################################################

"""
Listing sheets in Excel files

Specifically, you'll be loading and checking out the spreadsheet 'battledeath.xlsx', modified from the Peace Research Institute Oslo's (PRIO) dataset. 
This data contains age-adjusted mortality rates due to war in various countries over several years.

Instructions
- Assign the spreadsheet filename (provided above) to the variable file.
- Pass the correct argument to pd.ExcelFile() to load the file using pandas, assigning the result to the variable xls.
- Print the sheetnames of the Excel spreadsheet by passing the necessary argument to the print() function.

"""

# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'files/battledeath.xlsx'

# Load spreadsheet: xls
xls = pd.ExcelFile(file)

# Print sheet names
print(xls.sheet_names)

############################################################################################

"""
Importing sheets from Excel files

In the previous exercises, you saw that the Excel file contains two sheets, '2002' and '2004'. The next step is to import these.

In this exercise, you'll learn how to import any given sheet of your loaded .xlsx file as a DataFrame. 
You'll be able to do so by specifying either the sheet's name or its index.

Instructions
- Load the sheet '2004' into the DataFrame df1 using its name as a string.
- Print the head of df1 to the shell.
- Load the sheet 2002 into the DataFrame df2 using its index (0).
- Print the head of df2 to the shell.

"""

# Load a sheet into a DataFrame by name: df1
df1 = xls.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xls.parse(0)

# Print the head of the DataFrame df2
print(df2.head())

############################################################################################

"""
Customizing your spreadsheet import

Here, you'll parse your spreadsheets and use additional arguments to skip rows, rename columns and select only particular columns.

You'll add the additional arguments skiprows, names and usecols. These skip rows, name the columns and designate which columns to parse, respectively. 
All these arguments can be assigned to lists containing the specific row numbers, strings and column numbers, as appropriate.

Instructions
-   Parse the first sheet by index. In doing so, skip the first row of data and name the columns 'Country' and 'AAM due to War (2002)' using the argument names.
    The values passed to skiprows and names all need to be of type list.
-   Parse the second sheet by index. In doing so, parse only the first column with the usecols parameter, skip the first row and rename the column 'Country'.
    The argument passed to usecols also needs to be of type list.

"""

# Parse the first sheet and rename the columns: df1
df1 = xls.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
df2 = xls.parse(1, usecols=[0], skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())

############################################################################################

"""
Importing SAS files

In this exercise, you'll figure out how to import a SAS file as a DataFrame using SAS7BDAT and pandas. 
Both pandas and matplotlib.pyplot have already been imported as follows:

import pandas as pd
import matplotlib.pyplot as plt

The data are adapted from the website of the undergraduate text book Principles of Econometrics by Hill, Griffiths and Lim.

Instructions
- Import the module SAS7BDAT from the library sas7bdat.
- In the context of the file 'sales.sas7bdat', load its contents to a DataFrame df_sas, using the method .to_data_frame() on the object file.
- Print the head of the DataFrame df_sas.
- Execute your entire script to produce a histogram plot!

"""
import pandas as pd
import matplotlib.pyplot as plt

# Import sas7bdat package
from sas7bdat import SAS7BDAT

# Save file to a DataFrame: df_sas
with SAS7BDAT('files/sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())

# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()

############################################################################################

"""
Importing Stata files

Here, you'll gain expertise in importing Stata files as DataFrames using the pd.read_stata() function from pandas. 

Instructions
- Use pd.read_stata() to load the file 'disarea.dta' into the DataFrame df.
- Print the head of the DataFrame df.
- Visualize your results by plotting a histogram of the column disa10. We’ve already provided this code for you, so just run it!

"""

# Import pandas
import pandas as pd

# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('files/disarea.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
plt.show()

############################################################################################

