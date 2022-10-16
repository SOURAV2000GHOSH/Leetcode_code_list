# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=ListNode(-20)
        temp.next=head
        head=temp
        cur=head.next
        while cur.next:
            if not cur.next.next and cur.next.val==0:
                cur.next=None
                break
            if cur.next.val==0:
                cur=cur.next
            else:
                cur.val+=cur.next.val
                cur.next=cur.next.next
        return head.next
                