
""" 
return the largest perimeter of a 
triangle with a non-zero area, formed 
from three of these lengths. If it is 
impossible to form any triangle of a non-zero area,
return 0.
"""
#Runtime: 493 ms, faster than 16.95% of Python3 online submissions

def largestPerimeter(nums): 
    nums = sorted(nums)[::-1]
    length = len(nums)
    for x in range(length-2):
        if nums[x]< nums[x+1]+nums[x+2]:
            return nums[x]+nums[x+1]+nums[x+2]
    return 0

nums = [4,3,5,6,7,1]
print(largestPerimeter(nums))
