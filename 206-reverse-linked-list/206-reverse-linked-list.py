# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev,cur,nex=head,head.next,head.next.next
        while nex:
            cur.next=prev
            prev=cur
            cur=nex
            nex=nex.next
        cur.next=prev
        head.next=None
        return cur
        