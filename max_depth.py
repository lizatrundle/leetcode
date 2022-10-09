
#Given the root of a binary tree, return its maximum depth.
#46 ms faster than 90.38% of Python3 online submissions

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def maxDepth(self, root) -> int:
            if root is None:
                return 0
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            
            ans = max(left,right)+1
            
            return ans

