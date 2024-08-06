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

