# Generate a sorted array of 15 random integers
arr =[6, 7, 10, 15, 19, 25, 40, 41, 45, 54, 65, 80, 93, 94, 98]
x = 65

def RecursiveSearch(arr, x, arr.length):

    if arr[cursor] == x:
        return
    elif arr[cursor] > x:
        new_cursor = cursor + (0.5 * cursor)
    elif arr[cursor] < x:
        new_cursor = cursor - (0.5 * cursor)

    RecursiveSearch(arr, x, new_cursor)
