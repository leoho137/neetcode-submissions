# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()

        if not root:
            return res
        else:
            q.append(root)
        
        while q:
            count = len(q)
            temp = []
            for i in range(count):
                x = q.popleft()
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
                temp.append(x.val)
            res.append(temp)
        return res
            
