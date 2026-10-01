class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        arr = []
        numset = set(nums)
        def backtracking(l: int):
            if l == len(nums):
                res.append(arr.copy())
                return
            for n in nums:
                if n in numset:
                    arr.append(n)
                    numset.remove(n)
                    backtracking(l + 1)
                    arr.pop()
                    numset.add(n)


        backtracking(0)
        return res
            