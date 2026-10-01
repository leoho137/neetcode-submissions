class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = dict()
        for i in range(len(nums)):
            a[target - nums[i]] = i
        print(a)
        for x in nums:
            if x in a and nums.index(x) != a[x]: 
                return [nums.index(x), a[x]]
        