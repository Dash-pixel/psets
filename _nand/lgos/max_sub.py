# bad solution
def max_subarray_squared(nums):
    max_sum = 0
    for i in range(len(nums)):
        sum = 0
        for j in nums[i:]:
            sum += j
            if sum > max_sum:
                max_sum = sum
    return max_sum


# GOOD SOLUTION
def max_subarray_linear(nums):
    sum_ = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        if sum_ < 0:
            sum_ = 0

        sum_ += num

        if sum_ > max_sum:
            max_sum = sum_

    return max_sum


# maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
