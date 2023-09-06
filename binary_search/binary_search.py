class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            combined = (left + right) // 2
            if nums[combined] < target:
                left = combined + 1
            elif nums[combined] > target:
                right = combined - 1
            else:
                return combined

        return -1

result = Solution().search(nums = [-1,0,3,5,9,12], target = 9)
print(result)
