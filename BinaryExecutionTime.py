import random
import time
start_time = time.time()


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


############################# Execution Time in Worst case ##################################
# Worst case: element not in array
n = 140000
arr = [i for i in range(n)]
x = -2
result = binary_search(arr, x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

end_time = time.time()
execution_time = (end_time - start_time) * 1000
print(f"Time taken for Worst case: ", execution_time, "milliseconds")

"""
############################# Execution Time in Best case ##################################
# Best case: element in the middle of the array
n = 20000
arr = [i for i in range(n)]

x = n // 2
result = binary_search(arr, x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

end_time = time.time()
execution_time = (end_time - start_time) * 1000
print(f"Time taken for average case: ", execution_time, "milliseconds")

"""

"""
############################# Execution Time in Average case ##################################
# Average case: element at a random index in the array
n = 80000
arr = [i for i in range(n)]
x = random.randint(0, n - 1)
result = binary_search(arr, x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

end_time = time.time()
execution_time = (end_time - start_time) * 1000
print(f"Time taken for average case: ", execution_time, "milliseconds")

"""

