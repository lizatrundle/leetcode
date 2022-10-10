
    #Runtime: faster than 60.74% of Python3 online submissions
    #O(n) loop through array and compare cur sum to past sums, with a check for negative sums
    #simplistic approach
def maxSubArray(nums: list[int]) -> int:
    # max_sum = 0
    cur_sum = 0
    maximum_seen_so_far = nums[0]
    
    for x in range(len(nums)):
        cur_sum+= nums[x]
        if cur_sum < 0:
            if maximum_seen_so_far < cur_sum:
                maximum_seen_so_far = cur_sum
            cur_sum =0
        else:
            if maximum_seen_so_far < cur_sum:
                maximum_seen_so_far = cur_sum
    return maximum_seen_so_far

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))


        