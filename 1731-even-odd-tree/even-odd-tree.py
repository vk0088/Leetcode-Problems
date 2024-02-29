# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        l=0
        q=[root]

        while q:
            prev = float('-inf') if l%2 ==0 else float('inf')
            for _ in range(len(q)):
                temp = q.pop(0)
                if (l%2==0 and (temp.val %2==0 or temp.val <= prev)) or (l%2!=0 and(temp.val%2!=0 or temp.val >= prev)):
                    return False
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)

                prev=temp.val
            l+=1

        return True