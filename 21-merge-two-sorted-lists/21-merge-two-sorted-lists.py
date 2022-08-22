# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=list1
        l2=list2
        root=ListNode(-1000)
        temp=root
        while l1 and l2:
            if l1.val<l2.val:
                temp.next=ListNode(l1.val)
                l1=l1.next
                temp=temp.next
            elif l1.val>l2.val:
                temp.next=ListNode(l2.val)
                l2=l2.next
                temp=temp.next
            else:
                temp.next=ListNode(l1.val)
                temp=temp.next
                l1=l1.next
                temp.next=ListNode(l2.val)
                temp=temp.next
                l2=l2.next
        if not l1 and l2:
            temp.next=l2
        if not l2 and l1:
            temp.next=l1
        
        return root.next
                
                            
        