# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        ptr=head
        while ptr:
            count+=1
            ptr=ptr.next
        aim_node=count//2
        ptr=head
        while aim_node>0:
            ptr=ptr.next
            aim_node -= 1
        return ptr
        