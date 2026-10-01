class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Identify sequence starts
        s = set(nums)
        max = 0
        for n in nums:
            if n - 1 not in s:
                x = n + 1
                m = 1
                while x in s:
                    x += 1
                    m += 1
                if m > max:
                    max = m
        return max