import numpy as np

def diagonal_difference(matrix):
    left_to_right = np.trace(matrix)
    right_to_left = np.trace(np.fliplr(matrix))

    return abs(left_to_right - right_to_left)

print(diagonal_difference([[11, 2, 4], [4, 5, 6], [10, 8, -12]])) #15
print(diagonal_difference([[-1, 1, -7, -8], [-10, -8, -5, -2], [0, 9, 7, -1], [4, 4, -2, 1]])) #1

#3-26-2023
#space complexity - O(1)
#time complexity - O(n^2)
#form chatGPT with using numpy module