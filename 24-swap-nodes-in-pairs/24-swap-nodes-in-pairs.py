# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        prev,cur=head,head.next
        canswap=0
        while cur:
            if canswap==0:
                prev.val,cur.val=cur.val,prev.val
                canswap=1
                prev=cur
                cur=cur.next
                continue
            prev=cur
            cur=cur.next
            canswap=0
        return head