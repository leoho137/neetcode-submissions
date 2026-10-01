class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        j = 0
        k = len(heights) - 1
        while j < k:
            res = max(min(heights[j], heights[k]) * (k - j), res)
            if heights[j] > heights[k]:
                k -= 1
            else:
                j += 1
        return res