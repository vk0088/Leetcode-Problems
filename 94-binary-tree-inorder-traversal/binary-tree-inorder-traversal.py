# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    ### Recursive ####

        #out = []
        #def helper(root):
        #    if not root:
        #        return root
        #    helper(root.left)
        #    out.append(root.val)
        #    helper(root.right)

        #helper(root)
        #return out
    ### Time complexity O(log(n)). Space O(n)

    ###### Iterative approach ####
        out = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            out.append(curr.val)
            curr = curr.right
        return out
