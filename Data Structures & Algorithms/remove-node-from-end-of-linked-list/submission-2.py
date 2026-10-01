# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        if length == 1:
            return None
        if length == n:
            return head.next
        l = length - n
        temp = head
        for i in range(l - 1):
            temp = temp.next
        if temp.next:
            r = temp.next.next
            temp.next = r
        else:
            temp.next = None
        return head

