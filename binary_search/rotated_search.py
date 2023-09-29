class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            print(nums[mid])
            if nums[mid] == target:
                return mid
            
            # If we're before the rotation, or there is no rotation
            if nums[mid] >= nums[left]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            # We're in the section after the rotation
            else:
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1

result = Solution().search([1,3,5], 5)
# [0,1,2,3,4]
# result = Solution().search([4,5,6,7,0,1,2], 0)
print('found', result)
# result = Solution().search([1,3], 3)
# print(result)
