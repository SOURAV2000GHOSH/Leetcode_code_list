# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            prev,cur,nex=head,head.next,head.next.next
            while nex:
                cur.next=prev
                prev=cur
                cur=nex
                nex=nex.next
            cur.next=prev
            return cur,head
        
        if k<=1 or not head or not head.next:
            return head
        temp=ListNode(-1)
        temp.next=head
        head=temp
        ptr1=head
        
        while ptr1:
            ptr3=None
            ptr2=ptr1.next
            count=1
            while count < k:
                if not ptr2:
                    break
                ptr2=ptr2.next
                count+=1
            if count<k or not ptr2:
                break
            ptr3=ptr2.next
            ptr2.next=None
            start,end = reverse(ptr1.next)
            ptr1.next=start
            end.next=ptr3
            ptr1=end
        return head.next