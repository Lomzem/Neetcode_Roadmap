class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        beg_pointer = 0
        end_pointer = len(numbers) - 1
        
        while beg_pointer < end_pointer:
            if numbers[beg_pointer] + numbers[end_pointer] == target:
                return [beg_pointer + 1, end_pointer + 1]
            elif numbers[beg_pointer] + numbers[end_pointer] > target:
                end_pointer -= 1
            elif numbers[beg_pointer] + numbers[end_pointer] < target:
                beg_pointer += 1
