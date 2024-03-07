# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getsize(self,head:Optional[ListNode])->int:
        curr = head
        size = 0
        while(curr):
            curr = curr.next
            size += 1
        return size
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = self.getsize(head)
        middle = int(size/2) + 1
        curr = head
        while(middle != 1):
            curr = curr.next
            middle -= 1
        return curr