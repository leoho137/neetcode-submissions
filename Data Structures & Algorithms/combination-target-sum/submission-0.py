class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        arr = []
        def backtracking(x: int, total: int):
            if total == target:
                res.append(arr.copy())
                return
            if total < target:
                for i in range(x, len(nums)):
                    arr.append(nums[i])
                    backtracking(i, total + nums[i])
                    arr.pop()
                    
        
        backtracking(0, 0)
        return res