# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def finder(node, maxi,mini):
            nonlocal ans
            if not node:
                return     
            ans = max(ans, max(abs(node.val - maxi), abs(node.val - mini)))
            finder(node.left, max(node.val, maxi), min(node.val, mini))
            finder(node.right,max(node.val, maxi), min(node.val, mini))
        finder(root, root.val, root.val)
        return ans    
        