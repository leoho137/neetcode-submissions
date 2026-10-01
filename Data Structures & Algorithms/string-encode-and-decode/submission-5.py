class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            s = str(len(s)) + "#" + s
            res += s
        return res
    def decode(self, s: str) -> List[str]:
        print(s)
        n = ""
        count = -1
        res = []
        word = ""
        for c in s:
            if count > 0:
                word += c
                count -= 1
                continue
            if count == 0:
                res.append(word)
                word = ""
                count = -1
            if c != "#":
                n += c
                continue
            count = int(n)
            n = ""
        if count == 0:
            res.append(word)

        
        return res
