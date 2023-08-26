class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        results = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                three_sum = num + nums[j] + nums[k]
                if three_sum < 0 :
                    j += 1
                elif three_sum > 0:
                    k -= 1
                else:
                    results.append([num, nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return results

