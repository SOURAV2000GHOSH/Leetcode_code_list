# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        a=0
        j=l1
        k=l2
        new_list=ListNode(744)
        i=new_list
        while j and k:
            suma=j.val + k.val+a
            if suma >= 10:
                a=suma//10
                sumb = suma % 10
                i.next=ListNode(sumb)
                i=i.next
                j=j.next
                k=k.next
            else:
                a=0
                i.next=ListNode(suma)
                i=i.next
                j=j.next
                k=k.next
        while j:
            suma=j.val +a
            if suma >= 10:
                a=suma//10
                sumb = suma % 10
                i.next=ListNode(sumb)
                i=i.next
                j=j.next
            else:
                a=0            
                i.next=ListNode(suma)
                i=i.next
                j=j.next
        while k:
            suma=k.val +a
            if suma >= 10:
                a=suma//10
                sumb = suma % 10
                i.next=ListNode(sumb)
                i=i.next
                k=k.next
            else:
                a=0            
                i.next=ListNode(suma)
                i=i.next
                k=k.next
        if a==1:
            i.next=ListNode(1)
        return new_list.next