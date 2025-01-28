# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []  # Ensure res is a list to store results

        def paths(node, path, res):
            if node is not None:
                path += str(node.val)
                if node.left is None and node.right is None:
                    res.append(path)
                else:
                    path += "->"
                    paths(node.left, path, res)
                    paths(node.right, path, res)

        paths(root, "", res) 
        return res