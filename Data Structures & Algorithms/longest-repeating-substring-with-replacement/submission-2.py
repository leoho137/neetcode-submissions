class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        freq = dict()
        max_count = 0
        res = 0
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1
            max_count = max(max_count, freq[s[i]])
            if i - start + 1 > k + max_count:
                freq[s[start]] -= 1
                start += 1
            res = max(res, i - start + 1)
        return res