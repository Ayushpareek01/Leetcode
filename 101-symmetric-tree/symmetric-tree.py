# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        s1 = []
        s2 = []

        s1.append(root.left)
        s2.append(root.right)

        while s1 and s2:
            node1 = s1.pop()
            node2 = s2.pop()

            if node1 is None and node2 is None:
                continue

            if node1 is None or node2 is None or node1.val != node2.val:
                return False
            
            s1.append(node1.left)
            s2.append(node2.right)

            s1.append(node1.right)
            s2.append(node2.left)

        return len(s1) == 0 and len(s2) == 0