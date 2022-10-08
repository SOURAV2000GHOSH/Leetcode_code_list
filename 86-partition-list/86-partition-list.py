# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        if not head or not head.next:
            return head
        temp=ListNode(-200)
        temp.next=head
        head=temp
        prev,cur=head,head.next
        #make a cheaker to get first greater element to stop modifing m1,m2 pointer
        isgreat=False
        m1,m2=None,None
        while cur:
            if not isgreat and cur.val>=x:
                m1=prev
                m2=cur
                isgreat=True
                prev=cur
                cur=cur.next
                continue
            if isgreat and cur.val<x:
                prev.next=cur.next
                cur.next=m2
                m1.next=cur
                m1=m1.next
                cur=prev.next
                continue
            prev=cur
            cur=cur.next
        return head.next
                