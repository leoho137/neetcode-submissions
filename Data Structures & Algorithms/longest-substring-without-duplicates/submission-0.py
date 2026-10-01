class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        r, l = 0, 0
        res = 0
        for x in s:
            r += 1
            if x not in seen:
                seen.add(x)
            else:
                while s[l] != x:
                    seen.remove(s[l])
                    l += 1
                l += 1
            res = max(res, r - l)
        return res