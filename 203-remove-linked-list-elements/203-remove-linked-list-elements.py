# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        temp=ListNode(123)
        temp.next=head
        head=temp
        cur=head.next
        while cur:
            if cur.val==val:
                temp.next=cur.next
                cur=cur.next
                continue
            temp=cur
            cur=cur.next
        return head.next
        