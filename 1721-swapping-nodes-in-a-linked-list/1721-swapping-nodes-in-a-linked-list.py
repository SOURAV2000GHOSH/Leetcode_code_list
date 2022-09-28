# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count=0
        ptr=head
        while ptr:
            count+=1
            ptr=ptr.next
        sec_node=(count-k)+1
        ptr1=head
        while k>1:
            k-=1
            ptr1=ptr1.next
        ptr2=head
        while sec_node>1:
            sec_node-=1
            ptr2=ptr2.next
        ptr1.val,ptr2.val=ptr2.val,ptr1.val
        
        return head
        
        