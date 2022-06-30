# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: 
                return 0
            nonlocal diameter 
            left = dfs(root.left)
            right = dfs (root.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)
        diameter = 0
        dfs(root)
        return diameter
        