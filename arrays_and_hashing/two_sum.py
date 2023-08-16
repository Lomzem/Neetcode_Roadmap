class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen_nums = {}
        for i, num in enumerate(nums):
            pair = target - num
            if seen_nums.get(pair) is not None:
                return([seen_nums[pair], i])
            seen_nums[num] = i

