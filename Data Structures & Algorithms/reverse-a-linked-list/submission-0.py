# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = head
        prev = None
        while x:
            new = x.next
            x.next = prev
            prev = x
            x = new
        return prev