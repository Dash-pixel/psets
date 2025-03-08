class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, middle, j = 0, len(nums) // 2, len(nums) - 1

        while i < middle:

            if nums[i] > nums[middle]:
                j = middle

            elif nums[middle] > nums[j]:
                i = middle

            else:
                return nums[i]

            middle = (i + j) // 2

        return nums[j]
