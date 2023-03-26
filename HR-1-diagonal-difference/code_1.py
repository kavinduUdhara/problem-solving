def diagonalDifference(arr):
    left_to_right = 0
    right_to_left = 0
    
    for i in range(len(arr)):
        left_to_right += (arr[i][i])
    
    lenght = len(arr) - 1
    for i in range(len(arr)):
        right_to_left += (arr[i][lenght])
        lenght -= 1

    result = abs(left_to_right - right_to_left)
    return(result)

print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]])) #15
print(diagonalDifference([[-1, 1, -7, -8], [-10, -8, -5, -2], [0, 9, 7, -1], [4, 4, -2, 1]])) #1

#3-13-2023