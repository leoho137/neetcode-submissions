class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = dict()
        b = dict()
        for x in s:
            if x not in a:
                a[x] = 1
            else:
                a[x] += 1
        for y in t:
            if y not in b:
                b[y] = 1
            else:
                b[y] += 1
        if len(a) != len(b):
            return False
        for i in a:
            if i not in b:
                return False
            elif a[i] != b[i]:
                return False
        return True
            
