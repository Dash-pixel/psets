# Generate a sorted array of 15 random integers
arr =[6, 7, 10, 15, 19, 25, 40, 41, 45, 54, 65, 80, 93, 94, 98]
x = 65

def RecursiveSearch(arr, x, cursor):
    #find the middle of the array

    if arr[cursor] == x:
        return cursor

    elif arr[cursor] > x:
        cursor = round(0.5 * cursor)

    else:
        cursor = round(1.5 * cursor)

    RecursiveSearch(arr, x, cursor)
