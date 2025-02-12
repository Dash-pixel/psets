
def findMin(nums, target):
    # first create binary search
    # binary search in array -- find n
    i = 0
    j = len(nums) - 1
    tri = 0

    while True:
        if nums[tri] == target:
            return tri
        
        length = j - i
        tri = ((j-i)// 2) + i

        if target > nums[tri]:
            i = tri

        if target < nums[tri]:
            j = tri

 


            

            
