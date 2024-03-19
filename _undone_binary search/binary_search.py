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










RecursiveSearch(arr, x, (arr.length()/2))


# функция должна возвращать индекс
# maybe use some dumb counter

def RecursiveSearch(arr, x):

    counter = 0

    if arr[arr.length] == x:
        return counter

    elif arr[cursor] > x:
        cursor = round(0.5 * cursor)
        counter = 0.5 * array
        RecursiveSearch(arr, x)
    else:
        cursor = round(1.5 * cursor)
        RecursiveSearch(arr, x)

        counter +=1


# fibonacci should take in index and return the fibonacci number

fibonacci(1):
 return 1

fibonacci(2):
    return 1

def fibonacci(n):
    if n = 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
