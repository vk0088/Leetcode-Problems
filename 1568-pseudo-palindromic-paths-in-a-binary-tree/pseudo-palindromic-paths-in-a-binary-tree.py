# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans=0
        def count_palindrome_paths(node,cur):
            nonlocal ans
            if not node:
                return
            dummy=cur.copy()
            if node.val in dummy:
                dummy[node.val]-=1
                if dummy[node.val]==0:
                    del dummy[node.val]
            else:
                dummy[node.val]=1
            
            if not node.left and not node.right:
                if len(dummy)<=1:
                    ans+=1
            if node.left:
                # print(dummy)
                count_palindrome_paths(node.left,dummy)
            if node.right:
                # print(dummy)
                count_palindrome_paths(node.right,dummy)
        
        count_palindrome_paths(root,{})
        return ans

            
            

            
        
        