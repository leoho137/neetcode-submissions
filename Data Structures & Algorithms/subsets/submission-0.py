class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def addSubset(sub: List[int], n: int):
            if n == len(nums):
                res.append(sub)
                return
            addSubset(sub + [nums[n]], n + 1)
            addSubset(sub, n + 1)

        addSubset([], 0)
        return res

