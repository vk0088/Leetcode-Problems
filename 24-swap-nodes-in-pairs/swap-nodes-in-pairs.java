/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        if(head == null || head.next == null)
            return head;
       
        ListNode dummy = new ListNode(1, head); 
        ListNode prev = dummy;
        while( prev != null){
            ListNode left = null, right = null;
            if(prev.next == null)
                break;
            left = prev.next;
            if(left.next == null)
                break;
            right = left.next;
            left.next = right.next;
            right.next = prev.next;
            prev.next = right;
            
            prev = prev.next.next;
        }
        return dummy.next;
    }
}