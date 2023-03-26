def diagonalDifference(arr):
    left_to_right = 0
    right_to_left = 0
    
    len_of_arr = len(arr) #In general, it's a good practice to avoid calling len() in a loop if possible
    lenght = len(arr) - 1
    
    for i in range(len_of_arr):
        left_to_right += (arr[i][i])
        right_to_left += (arr[i][lenght])
        lenght -= 1     

    result = abs(left_to_right - right_to_left)
    return(result)

print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]])) #15
print(diagonalDifference([[-1, 1, -7, -8], [-10, -8, -5, -2], [0, 9, 7, -1], [4, 4, -2, 1]])) #1

#3-26-2023
#space complexity - O(1)
#time complexity - O(n)
