class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            a = [0] * 26
            for x in s:
                a[ord(x) - ord('a')] += 1
            if tuple(a) not in d:
                d[tuple(a)] = [s]
            else:
                d[tuple(a)].append(s)
        
        return list(d.values())