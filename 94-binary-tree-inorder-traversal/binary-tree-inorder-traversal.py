# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#        res = []
#        if not root:
#            return []        
#        res = self.inorderTraversal(root.left) 
#        res.append(root.val)                   
#        res.extend(self.inorderTraversal(root.right))
#        return res
        inorder = []
        stack = []
        
        while True:
            if root:
                stack.append(root)
                root = root.left
            else:
                if not stack:
                    break
                root = stack.pop()
                inorder.append(root.val)
                root = root.right
        
        return inorder      

        