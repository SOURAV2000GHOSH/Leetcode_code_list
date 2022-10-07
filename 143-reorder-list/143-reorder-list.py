# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(head):
            if not head or not head.next:
                return head,head
            prev,cur,nex=head,head.next,head.next.next
            while nex:
                cur.next=prev
                prev=cur
                cur=nex
                nex=nex.next
            cur.next=prev
            return cur,head
        if not head or not head.next or not head.next.next:
            return head
        slow=fast=prev=head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
            
        prev=slow
        slow=slow.next
        prev.next=None
        start,end=reverse(slow)
        end.next=prev
        cur=head
        p1=head
        p2=head.next
        s1=start
        s2=start.next
        while s2:
            p1.next=s1
            s1.next=p2
            p1=p2
            s1=s2
            p2=p2.next
            s2=s2.next
        return head