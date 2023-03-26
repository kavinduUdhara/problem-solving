def miniMaxSum(arr):
    arr = sorted(arr)  # O(n log n)
    sum1 = arr[1:]     # O(n)
    sum2 = arr[:-1]    # O(n)

    sum1total = 0      # O(1)
    for n in sum1:     # O(n)
        sum1total += n # O(1)

    sum2total = 0      # O(1)
    for n in sum2:     # O(n)
        sum2total += n # O(1)

    print("{} {}".format(sum2total, sum1total)) # O(1)

print(miniMaxSum([1, 2, 3, 4, 5])) #10 14
print(miniMaxSum([396285104, 573261094, 759641832, 819230764, 364801279])) #2093989309 2548418794
print(miniMaxSum([140638725, 436257910, 953274816, 734065819, 362748590])) 


#time complexity O(nlogn)