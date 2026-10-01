# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        temp = res
        r = 0
        while set(lists) and set(lists) != {None}:
            minval = 1000
            for x in lists:
                if x and minval >= x.val:
                    r = lists.index(x)
                    minval = x.val
            temp.next = lists[r]
            temp = temp.next
            lists[r] = lists[r].next
            

        return res.next
