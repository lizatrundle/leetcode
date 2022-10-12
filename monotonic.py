'''
Given an integer array nums, 
return true if the given array is monotonic,
 or false otherwise.
'''

#Runtime: 1056 ms, faster than 90.64% of Python3 online submissions
def isMonotonic(nums: list[int]) -> bool:
    forward = sorted(nums)
    backward = sorted(nums)[::-1]
    if nums == forward or nums ==backward:
        return True 
    return False

arr = [6,5,4,4]
print(isMonotonic(arr))
