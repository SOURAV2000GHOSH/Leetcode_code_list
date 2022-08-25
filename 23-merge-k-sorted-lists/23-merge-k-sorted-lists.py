# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, l: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp=[]
        
        #store all the value of linked list
        for x in l:
            ptr=x
            while ptr:
                temp.append(ptr.val)
                ptr=ptr.next
                
        temp.sort()
        head=ListNode(-432324)
        ptr=head
        
        #make tree node
        for el in temp:
            ptr.next=ListNode(el)
            ptr=ptr.next
        
        return head.next