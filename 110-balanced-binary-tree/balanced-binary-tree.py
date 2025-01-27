# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root):
        if root is None:
            return 0
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        
        return max(lheight, rheight) + 1
   
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        lheight = self.height(root.left)
        rheight = self.height(root.right)

        if abs(lheight - rheight) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
       
        l
        