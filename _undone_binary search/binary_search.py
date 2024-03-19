# Generate a sorted array of 15 random integers
arr =[6, 7, 10, 15, 19, 25, 40, 41, 45, 54, 65, 80, 93, 94, 98]
x = 65

def RecursiveSearch(arr, x):
    #find the middle of the array
    cursor= arr.length / 2

    if arr[cursor] == x:
        return cursor

    elif arr[cursor] > x:
        RecursiveSearch(arr)
