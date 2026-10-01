class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        d = dict()
        res = []
        for x in nums:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        for y in d:
            bucket[d[y]].append(y)
        print(bucket)
        count = 0
        for x in reversed(bucket):
            if x:
                res.extend(x)
                count += len(x)
            if count == k:
                break
        return res
