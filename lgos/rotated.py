class Solution:
    def findMin(self, nums): #: List[int]) -> int:
        #[3,4,5,1,2]
        i = 0
        j = len(nums) - 1

        while True:

            middle = ((j-i)//2) + i

            

            if j == i+1:
                if nums[j] > nums[0]:
                    return nums[0]
                return nums[j]
            
            if nums[i] > nums[middle]:
                j = middle
            
            if nums[i] < nums[middle]:
                i = middle
            

