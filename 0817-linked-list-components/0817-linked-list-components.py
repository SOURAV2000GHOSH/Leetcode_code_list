# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        cheak=set(nums)
        connected=False
        ptr=head
        count=0
        while ptr:
            if ptr.val in cheak and not connected:
                count+=1
                connected=True
            if ptr.val not in cheak:
                connected=False
            ptr=ptr.next
        
        return count
        
        