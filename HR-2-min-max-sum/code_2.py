def miniMaxSum(arr):
    arr_sum = sum(arr)
    min_val = arr_sum - max(arr)
    max_val = arr_sum - min(arr)
    print(min_val, max_val)


print(miniMaxSum([1, 2, 3, 4, 5])) #10 14
print(miniMaxSum([396285104, 573261094, 759641832, 819230764, 364801279])) #2093989309 2548418794