#return the element that appears the most in the array 
# runtime beats 95.40% of python3 submissions

def majorityElement(nums) -> int:
        counts = {}
        for x in nums:
            if x in counts:
                counts[x]+=1
            else:
                counts[x]=1
        max_num = 0
        key = 0
        for x in counts.keys():
            if counts[x]>max_num:
                max_num=counts[x]
                key = x
        return key
