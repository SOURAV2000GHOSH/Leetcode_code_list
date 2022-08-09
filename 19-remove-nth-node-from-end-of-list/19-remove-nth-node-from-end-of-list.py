# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        ptr1=head
        count=0
        while ptr1:
            ptr1=ptr1.next
            count += 1
        if count == n:
            return head.next
        count=count - n + 1
        ptr2=head.next
        ptr1=head
        while count > 2 and ptr2:
            ptr2=ptr2.next
            ptr1=ptr1.next
            count -= 1
        ptr1.next=ptr2.next
        return head
        