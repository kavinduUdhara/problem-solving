def max_subarray_sum(arr):
    contiguous_arrays =[]
    for number in range(len(arr)):
        contiguous_arrays.append(arr[:number])
    print(contiguous_arrays)

arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_subarray_sum(arr1)