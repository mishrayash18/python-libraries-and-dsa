"nd array creation"
# import numpy as np
# arr1 = np.array([1,2,3,4])
# print(arr1)



"1D array creation"
# import numpy as np
# arr1d = np.array([1,2,3,4])
# print(arr1d)



"nD array creation"
# import numpy as np
# arr2d = np.array([[1,2],[3,4]])
# arr3d = np.array([[1,2],[3,4],[5,6],[8,9]])
# n = int(input("enter the range of the array: "))
# arrnd = np.array([x for x in range(0, n)])
# print(arrnd)



"array indexing and slicing"
# import numpy as np
# arr = np.array([
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ])

# sub_arr = arr[0:2, 2:4]
# print(sub_arr)
"slicing creates a view, does not take any memory"
# safe_copy = arr[1:4, 0:2].copy()
# print(safe_copy)
"creates new memory for the new copied sub array or original array"



"""vectorization - it is the process of applying math operations
without traversing the whole datastructure (mutable)"""
# import numpy as np
# arr = np.array([10,20,30,40])
# print(arr+5)
# print(arr//5)
# print(arr*2)



"""broadcasting - applying mathematical operations on matrices
(arrays) of disimilar shapes"""
# import numpy as np
# mat1 = np.array([[1],[2],[3],[4]])
# mat2 = np.array([10,20,30,40])
# print(mat1+mat2)



"reshaping, filtering and stacking"
# import numpy as np
# mat1 = np.arange(10)
"""fills elements from 0 to 9 in the matrix"""

# mat2 = mat1.reshape(2,-1)
"reshapes the matrix,, -1 is for the function to decide itself"
"how many columns/rows to choose(columns in this case)"
# print(mat1)
# print(mat2)

"""vstack - used for stacking two arrays vertically"""
# import numpy as np
# row1 = ([10,20,30,40])
# row2 = ([50,60,70,80])
# vertical = np.vstack((row1, row2))
# print(vertical)

"hstack - used for stacking two arrays horizontally"
# horizontal = np.hstack((row1, row2))
# print(horizontal)



"boolean masking"
# import numpy as np
# arr = np.array([11, 45, 23, 37, 77, 19])
# arr = arr[arr>30]
# print(arr)

"mask-boolean values"
# mask = arr>30
# print(mask)
# print(arr[mask])



"linear algebra and aggregations"
# import numpy as np
# matrix = np.array([[1,2],[3,4]])

"aggregations col->axis=0, row->axis=1"
# column_sum = matrix.sum(axis=0)
# row_sum = matrix.sum(axis=1)
# print(column_sum)
# print(row_sum)

"linear algebra multiplications on the matrices"
# matrix2 = np.array([[2,0], [5,6]])
# multiply = matrix @ matrix2
# print(multiply)






"""You are given a 1D array of 14 elements. Your goal is to
shape it into a 2D matrix with exactly 4 columns. Because 14
elements cannot be split evenly into columns of 4, you must
first pad the end of the original array with zeros (0) until
it has the minimum number of elements required to reshape it
cleanly. Finally, reshape it using automatic row calculation(-1)."""
# import numpy as np
# arr = np.array([12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51])

# padded_arr = np.pad(arr, pad_width=(0, 4-(len(arr)%4)), mode="constant", constant_values=0)
# padded_arr2D = padded_arr.reshape(4,4)
# print(padded_arr2D)





"""You have two 2D matrices representing two different data batches.
Matrix A has a shape of (3, 2) and Matrix B has a shape of (3, 4).
Write the NumPy command to stitch these two matrices together horizontally
so that they form a single unified feature matrix. What is the final shape
of the combined matrix?"""
# import numpy as np
# matA = np.ones(shape=(3,2), dtype=int)
# matB = np.ones(shape=(3,4), dtype=int)
# matunified = np.hstack((matA, matB))
# print(matunified)





"""Given a 1D array of random integers, perform an in-place modification
using a boolean mask. You need to replace all numbers that are strictly
greater than 50 AND are even numbers with the value -1. All other numbers
must remain completely untouched."""
# import numpy as np
# # arr = np.random.randint(0, 101, 15)
# arr = np.array([42,87,15,63,8,91,29,74,55,12,99,36,47,20,68])

# mask = (arr>50) & (arr%2!=0)
# arr[~mask]=-1
# print(arr)





"""You are given a 5x5 matrix of sequential integers from 1 to 25.
Use 2D array slicing to extract a smaller 3x3 sub-matrix from the
exact center of the original matrix (dropping the top, bottom, leftmost,
and rightmost outer rows/columns)."""
# import numpy as np
# arr = np.arange(1,26).reshape(5,5)
# subarr = arr[1:4, 1:4].copy()
# print(subarr)





"""You have a 3x3 matrix. Find the maximum value along axis 1
(horizontally across columns for each row). Then, subtract that
row's maximum value from every element in that respective row using
broadcasting rules."""
# import numpy as np
# arr = np.array([[10,20,30],
#                [40,50,60],
#                [70,80,90]])

# rowmax = arr.max(axis=1, keepdims=True)
# newarr = arr-rowmax
# print(newarr)