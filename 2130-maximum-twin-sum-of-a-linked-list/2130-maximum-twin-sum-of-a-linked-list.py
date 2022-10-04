# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverse_linkedlist(head):
            if not head or not head.next:
                return head
            prev,cur,nex=head,head.next,head.next.next
            while nex:
                cur.next=prev
                prev=cur
                cur=nex
                nex=nex.next
            cur.next=prev
            return cur
        twin_sum=0
        prev=slow=fast=head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        end=reverse_linkedlist(prev.next)
        ptr1=head
        ptr2=end
        while ptr1.next != ptr2 :
            temp=ptr1.val+ptr2.val
            if twin_sum < temp:
                twin_sum=temp
            ptr1=ptr1.next
            ptr2=ptr2.next
        if (ptr1.val+ptr2.val) > twin_sum:
            twin_sum = (ptr1.val+ptr2.val)
        return twin_sum