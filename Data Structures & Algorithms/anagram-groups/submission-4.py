class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = dict()
        res = []
        for x in strs:
            t = str(sorted(x))
            if t not in words:
                words[t] = [x]
            else:
                words[t].append(x)
        for w in words:
            res.append(words[w])
        print(w)
        return(res)