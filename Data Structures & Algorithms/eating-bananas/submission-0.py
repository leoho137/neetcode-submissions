import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        k = max(piles)
        
        l, r = 1, k
        res = k

        while l <= r:
            total = 0
            k = (l + r) // 2
            for p in piles:
                total += math.ceil(p / k)
            if total <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

            
        return res

