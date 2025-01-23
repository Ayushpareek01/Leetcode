# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        curr = head
        if not head or k == 0:
            return head
        while curr is not None:
            arr.append(curr.val)
            curr = curr.next
        n = len(arr)
        k = k %n
        rotae_arr = arr[-k:] + arr[:-k]

        dummy = ListNode(0)
        curr = dummy
        for val in rotae_arr:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next