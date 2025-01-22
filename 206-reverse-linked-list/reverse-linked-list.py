# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        return prev 
    def push(self, head: Optional[ListNode], new_data: int) -> ListNode:
        new_node = Node(new_data) 
        new_node.next = head 
        return new_node
    def printList(self, head: Optional[ListNode]) -> None:
        temp = head 
        while(temp): 
            print (temp.data,end=" ") 
            temp = temp.next
        