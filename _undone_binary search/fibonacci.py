def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        number = fibonacci(n-1) + fibonacci(n-2)
        return number

fibonacci(10)


#solve without calling twice using dictionaries
# so fibonacci(n-1) contains fibonacci(n-2)

"""
how can we use dictionaries:
so we can just record the values, no?
"""
