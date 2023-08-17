class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1 for i in range(len(nums))]

        prefix = 1
        for i in range(len(nums)):
            result[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums), 0, -1):
            result[i - 1] *= postfix
            postfix *= nums[i - 1]

        return result

test = Solution()
nums = [1,2,3,4]
test.productExceptSelf(nums)
