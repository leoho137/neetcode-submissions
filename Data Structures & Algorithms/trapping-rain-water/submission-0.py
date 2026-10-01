class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        # find left and right bars
        left = [0 for _ in range(len(height))]
        right = [0 for _ in range(len(height))]
        for i in range(1, len(height) - 1):
            left[i] = max(height[i - 1], left[i - 1])
        for j in range((len(height) - 2), 0, -1):
            right[j] = max(height[j + 1], right[j + 1])
        for n in range(len(height)):
            res += max(min(left[n], right[n]) - height[n], 0)
            print(left[n], right[n], height[n])

        return res