class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        results = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    results.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return results
