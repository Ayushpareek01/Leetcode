# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode(-1)
        s = small
        big = ListNode(-1)
        b = big

        temp = head
        while temp:
            if temp.val < x:
                s.next = ListNode(temp.val)
                s = s.next
            else:
                b.next = ListNode(temp.val)
                b = b.next
            temp = temp.next
        s.next = big.next 
        b.next = None
        
        return small.next


        
