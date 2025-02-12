# import random
# arr = sorted([random.randint(1, 100) for _ in range(10)])
# print(arr)

def binary_search(arr: list, targ: int) -> int:
    i = len(arr)//2
    curr_size = i
    #did this exersise for one reason only - so that there is no questions about why did i delete such an easy excersize in my committs
    #it is too easy for my current level

    while arr[i] is not targ:
        curr_size //= 2

        if arr[i] > targ:
            i -= max(curr_size, 1)

        if arr[i] < targ:
            i += max(curr_size, 1)

        if arr[i] == targ:
            break

        if not curr_size:
            return('not found')

    return i

arr = [6, 21, 31, 33, 45]

# binary_search(arr, 6)
for i in range(len(arr)):
    print(f'i = {i} {binary_search(arr, arr[i])}')
