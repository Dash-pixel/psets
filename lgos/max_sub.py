def maxSubArray(nums):
    pref_sum = 0
    suff_sum = 0
    prefex = []
    suffix = []

    for element in nums:
        pref_sum += element
        prefex.append(pref_sum)
    
    for element in nums[::-1]:
        suff_sum += element
        suffix.append(suff_sum)
    
    #tuples 
    max_pref = max(enumerate(prefex), key = lambda x: x[1])
    max_suff = max(enumerate(suffix[::-1]), key = lambda x: x[1])

    if max_pref[0] > max_suff[0]:
        print(nums[max_suff[0]: max_pref[0]+1])
        return sum(nums[max_suff[0]: max_pref[0]+1])
    else:
        print(max_pref)
        print(max_suff)
        
        pass


maxSubArray([2, 3, 1, -2, -3, -4, 5, 1, 1, -1])
