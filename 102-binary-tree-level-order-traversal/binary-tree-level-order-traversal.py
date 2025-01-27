# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def Traversal(node, level):
            
            if not node:
                return []
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            Traversal(node.left, level + 1)
            Traversal(node.right, level + 1)
        Traversal(root,0)
        return res
            