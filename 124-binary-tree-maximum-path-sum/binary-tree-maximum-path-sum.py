# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')  
        
        def helper(node):
            if not node:
                return 0
            left = max(0, helper(node.left)) 
            right = max(0, helper(node.right))
            
            self.max_sum = max(self.max_sum, left + right + node.val)
            return node.val + max(left, right)
        
        helper(root)
        return self.max_sum
        
        