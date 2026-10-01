class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        mid = int(len(nums) / 2)
        if nums[l] < nums[r]:
            return nums[l]
        while r - l > 1:
            if nums[l] > nums[mid]:
                r = mid
            else:
                l = mid
            mid = int((l + r) / 2)
        return nums[r]