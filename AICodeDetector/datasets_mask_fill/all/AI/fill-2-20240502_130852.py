import numpy as np

def matrix_multiplication(matrix1, matrix2):
   return np.dot(matrix1, matrix2)

# 例
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

result = matrix_multiplication(matrix1, matrix2)
print("Result of matrix multiplication:")
print(result)
