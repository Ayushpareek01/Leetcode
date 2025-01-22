# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head 
        length = 0
        
        while temp is not None:
            temp = temp.next
            length += 1
        length1 = length - n
        temp = head
        if length1 == 0:
            haed = head.next
            return head.next
        while length1 > 1:
            temp = temp.next
            length1 -= 1
        
        temp.next = temp.next.next
        return head
                