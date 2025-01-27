# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = [root]
        res = []
        if not root:
            return []
        while st:
            root = st.pop()
            res.append(root.val)

            if root.right:
                st.append(root.right)
            if root.left:
                st.append(root.left)
            
        return res

