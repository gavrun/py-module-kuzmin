import numpy as np

# Working with arrays

lst = [7, 8]
arrlst = np.array(lst) # List-based array
""" Array () function accepts any sequence of elements """
print("The massif-vector on the list: ", arrlst)

array1 = np.arange(10) # Vector of entire numbers from 0 to 9
""" Arange () function creates an array based on a numerical sequence """
array2 = np.arange(5, 15)
array3 = np.arange(1, 5, 0.5)
print("Messions on Range:\n", array1,"\n", array2,"\n", array3)

arr1 = array1*2
arr2 = array1*array2
print("array1*2:\n", arr1,"\narray1*array2:\n", arr2)
print("Application of the function 'sin' to the elements of the array:\n", np.sin(array1)) # Numpy functions
print("Application of the function 'sum' to the elements of the array:\n", np.sum(array1))
print("The original array 'Array1':\n", array1)
print("Application of the function 'mean' to the array:", array1.mean()) # Massive functions


nd_array = np.array([[1,2],
                    [3,4]])
print("Two -dimensional array:\n", nd_array)
print("The number of elements:", nd_array.size)

nd_array2 = np.array([[5,6],
                    [7,8]])
print("Another two -dimensional array:\n", nd_array2)
nd_arrayS = nd_array + nd_array2
print("Operation '+' with two -dimensional arrays:\n", nd_arrayS)


# Work with matrices

"""
np.matrix()
Matrix is ​​a convenient tool for setting the matrix.
At the same time, you can transmit the Python list or the Numpy array as an argument.
"""
a = [[1, 2], [3, 4]] # List as the basis for the matrix
matr1 = np.matrix(a)
print("Matrix:\n", matr1)

matr11 = np.matrix('[1, 2; 3, 4]') # Creating in 'Matlab' style
#print("Matrix:\n", matr11)

m = np.array([[5, 6], [7, 8]]) #  Based on the Numpy array
matr2 = np.matrix(m)
print("Matrix:\n", matr2)

m1m2 = matr1 + matr2 # Addition of matrices
m1m2 = matr1 - matr2 # Subtraction of matrices
m1k = matr1 * 7      # Multiplication of the matrix by the number
m1m2 = matr1*matr2   # Multiplication of matrices
m1m2 = matr1.dot(matr2)
print("The sum of matrices:\n", m1m2)
print("Multiplication of the matrix by 7:\n", m1k)

m1T = matr1.T  # Transporation of matrices
m2T = np.transpose(matr2)
print("The original matrix:\n", m1T, "\nIts transposition:\n", m2T)

arWhere = np.where(array1 % 2 == 0, array1 * 10, array1 / 10) # The function returns one of the two specified elements depending on the condition
print (arWhere) #Man elements multiplies by 10, divides by 0

# An example of the implementation of data processing using threshold function.
a = np.random.rand(10)
print(a)
ap1 = np.where(a > 0.95, True, False)
print(ap1)
ap2 = np.where(a > 0.95, 1, -1)
print(ap2)

import matplotlib.pyplot as plt
plt.title('Stock Prices of Largest Software Companies')
plt.xlabel('Dates')
plt.ylabel('Stock Price')
plt.plot(array1, array2, color="r", marker="*", linestyle="none")
plt.show()
