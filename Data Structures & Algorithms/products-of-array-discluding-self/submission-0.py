class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [], []
        product = 1
        res = []
        for n in nums:
            product *= n
            prefix.append(product)
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            product *= nums[i]
            suffix.append(product)
        suffix = suffix[::-1]
        for j in range(len(nums)):
            if j == 0:
                product = suffix[1]
            elif j == len(nums) - 1:
                product = prefix[-2]
            else:
                product = suffix[j + 1] * prefix[j - 1]
            res.append(product)
        return res