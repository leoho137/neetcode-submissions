class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            p1 = i + 1
            p2 = len(nums) - 1
            while p1 != p2:
                if nums[p1] + nums[p2] == -nums[i]:
                    if [nums[i], nums[p1], nums[p2]] not in res:
                        res.append([nums[i], nums[p1], nums[p2]])
                    p1 += 1
                elif nums[p1] + nums[p2] < -nums[i]:
                    p1 += 1
                elif nums[p1] + nums[p2] > -nums[i]:
                    p2 -= 1

        return res