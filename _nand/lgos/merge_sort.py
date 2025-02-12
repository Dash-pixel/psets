#Time Complexity: Best Case: O(n log n)
#Space Complexity: Merge Sort requires additional space to store the merged subarrays during the merge process.
import random
import copy

def merge_arr(arr: list):
    chunk = 1
    arr_2 = [None] * len(arr)
    while chunk < len(arr):
        i = k = 0
        while k < len(arr):
            j = j_start = i + chunk

            while k < j_start + chunk and k < len(arr):
                #print(f'i={i} j={j} k={k}')
                if j >= len(arr):
                    arr_2[k] = arr[i]
                    i += 1
                    k += 1
                    continue

                if i < j_start and (arr[i] < arr[j] or j >= j_start + chunk):
                    arr_2[k] = arr[i]
                    i += 1
                    k += 1
                else:
                    arr_2[k] = arr[j]
                    j += 1
                    k += 1
                
            i = k
        arr = copy.deepcopy(arr_2)
        chunk *= 2


    return arr

random_array = [random.randint(1, 100) for _ in range(100)]
print(random_array)
print(merge_arr(random_array))

#so its jumping, but it should go through all the itterations