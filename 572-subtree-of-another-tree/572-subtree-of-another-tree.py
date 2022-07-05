# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q:return True
        if not p: return False
        if self.sameTree(p,q):
            return True 
        else:
            return (self.isSubtree(p.left, q) or self.isSubtree(p.right, q))
        
    def sameTree(self,p,q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        return False
        