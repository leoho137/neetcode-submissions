class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # count each letter
        a = dict()
        b = dict()
        for x in s1:
            if x in a:
                a[x] += 1
            else:
                a[x] = 1
        for j in range(len(s2)):
            if s2[j] in b:
                b[s2[j]] += 1
            else:
                b[s2[j]] = 1
            if j >= len(s1):
                b[s2[j - len(s1)]] -= 1
                if b[s2[j - len(s1)]] == 0:
                    del b[s2[j - len(s1)]]
            if a == b:
                return True
        return False