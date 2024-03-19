class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        que = []

        left = 0
        for right, rnum in enumerate(nums):
            while que and rnum > nums[que[-1]]:
                que.pop(-1)

            que.append(right)

            if left > que[0]:
                que.pop(0)

            if (right - left + 1) == k:
                result.append(nums[que[0]])
                left += 1

        return result
        print(result)


nums = [1, 3, 1, 2, 0, 5]
k = 3
# nums = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3
result = Solution().maxSlidingWindow(nums, k)
