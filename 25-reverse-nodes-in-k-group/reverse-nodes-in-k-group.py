# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        i=head

        def check(v,k):
            for _ in range(k):
                if v==None:
                    return False
                v=v.next
            return True

        def reverse(start,k):
            p=None
            i=start

            for _ in range(k):
                n=i.next
                i.next=p
                p,i=i,n

            return p, start, i

        base=ListNode()
        p=base
        n=head

        while check(n,k):
            i,j,n=reverse(n,k)
            p.next=i
            p=j

        p.next=n
        return base.next