# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
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
        
        if not head.next:
            return True
        count=0
        temp=head
        while temp:
            count+=1
            temp=temp.next
        count=count//2
        temp=head
        while count>1:
            count-=1
            temp=temp.next
        head2=reverse(temp.next)
        temp.next=None
        head1=head
        while head1:
            if head1.val != head2.val:
                return False
            head1=head1.next
            head2=head2.next
        return True
        
        
            
        
        