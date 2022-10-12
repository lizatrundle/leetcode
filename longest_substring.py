"""
Given a string s, find the length of 
the longest substring
 without repeating characters.
"""
#sliding window
#Runtime: 103 ms, faster than 69.26% of Python3 online submissions
def lengthOfLongestSubstring( s: str) -> int:
    left = 0
    right = 0
    longest = 0
    characters = set()
    length = len(s)

    while right<length:
        if s[right] not in characters:
            characters.add(s[right])
            right+=1
            longest = max(len(characters), longest)
        else:
            characters.remove(s[left])
            left+=1
    return longest


        









    
#     #creating a hashmap of characters that have been seen, ie. duplicates
#     duplicates = {}
#     left_index = 0
#     right_index = 0
#     substring = 0
#     length = len(s)        
#     #while both of them are still in the array, if they go off it is no longer valid subarray 
#     while left_index < length and right_index < length:
#         #current character is the string at the right index--starts at zero
#         current = s[right_index]            
#         # if the character has been seen before 
#         if current in duplicates:
#             #change the left index to be the maximum of either the index or the nidex of the duplicate char 
#             #whichever one is closest to the right 
#             left_index = max(left_index, duplicates[current] + 1)
#         #if its in duplicates then move the left over, and ignore 
#         #either way, move the right index one over each time 
#         duplicates[current] = right_index
#         substring = max(substring, right_index - left_index + 1)
#         right_index += 1
#     return substring

# string ="au"
# print(lengthOfLongestSubstring(string))
