n = 3

rod_a = list(range(n, 0, -1))
rod_b = []
rod_c = []

def sorting(n):
"""
     move n-1 to non-target rod -- here we should call the function recursivelly
     move the n'th rod to target rod
     move n-1 rod to target rod
     we need to think where is it recursivelly called

     rod_c.append(rod_a[-1])
     rod_a = rod_a[:-1]
"""
#quite importaint that with tower of hanoi of 3 we want to place the first bagel on the futherest rod
#but with 4 on the closesed
# because odd and even - we want to finish on the futherest away
# in 1 .. 1 move to C
# in 2 .. 1 move to B -- 2 move to C
# in 3 .. 1 move to C -- 2 move to B -- 1 move to C
