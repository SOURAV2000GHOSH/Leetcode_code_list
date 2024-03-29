# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        ptr=head
        count=1
        #counting number nodes
        while ptr.next:
            count+=1
            ptr=ptr.next
        isEven=False
        prev=cur=head
        
        #cheak even or odd number of nodes
        cheak=count%2==0
        
        #modifing linkedlist
        while count>1:
            if isEven:
                prev.next=cur.next
                cur.next=None
                ptr.next=cur
                ptr=ptr.next
                isEven=False
                cur=prev.next
                count-=1
            else:
                isEven=True
                prev=cur
                cur=cur.next
                count-=1
        #if linkedlist have even number of nodes then this block will will run
        if cheak:
            prev.next=cur.next
            cur.next=None
            ptr.next=cur
                
        return head
        