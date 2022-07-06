# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        def dfs(root, maxPath):
            if not root:
                return 0
            if root.val >= maxPath:
                return 1 + dfs(root.left , max(maxPath, root.val)) + dfs(root.right, max(maxPath, root.val))
            else:
                return 0 +  dfs(root.left , maxPath) + dfs(root.right, maxPath)
        
            
            
            
            
            
        
        maxPath = root.val
        res = 1 + dfs(root.left, maxPath) + dfs(root.right, maxPath)
        return res