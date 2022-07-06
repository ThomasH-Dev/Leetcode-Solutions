# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def bfs(root, left, right):
            if not root: return True
            if not (root.val < right and root.val > left):
                return False
            else:
                return (bfs(root.left, left ,root.val) and bfs(root.right, root.val, right))
        left = float("-inf")
        right = float("inf")     
        return bfs(root, left,right)