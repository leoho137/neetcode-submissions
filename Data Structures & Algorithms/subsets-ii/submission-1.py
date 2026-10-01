class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        arr = []
        nums.sort()
        def backtracking(l):
            if l == len(nums):
                res.append(arr.copy())
                return
            
            arr.append(nums[l])
            backtracking(l + 1)
            arr.pop()
            while l + 1 < len(nums) and nums[l] == nums[l + 1]:
                l += 1
            backtracking(l + 1)
        
        backtracking(0)
        return res