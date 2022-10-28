# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=ListNode(-60000)
        temp.next=head
        head=temp
        prev,cur=head,head.next
        
        while cur:
            if prev.val<=cur.val:
                prev=cur
                cur=cur.next
                continue
            check=head
            while check.next:
                if check.next is not None and check.next.val>cur.val:
                    break
                check=check.next
           
            prev.next=cur.next
            cur.next=check.next
            check.next=cur
            cur=prev.next
            
        return head.next
        