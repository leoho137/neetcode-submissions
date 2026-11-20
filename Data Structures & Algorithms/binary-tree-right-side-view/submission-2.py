# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = deque([root])
        res = []
        while stack:
            for i in range(len(stack)):
                curr = stack.popleft()
                if curr.left:
                    stack.append(curr.left) 
                if curr.right:
                    stack.append(curr.right)
            res.append(curr.val)
        return res

        