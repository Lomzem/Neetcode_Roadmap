class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        allowed = '1234567890abcdefghijklmnopqrstuvwxyz'
        allowed_string = ''.join([char for char in s if char in allowed])

        beg_pointer = 0
        end_pointer = len(allowed_string) - 1

        while beg_pointer < end_pointer:
            if allowed_string[beg_pointer] != allowed_string[end_pointer]:
                return False
            beg_pointer += 1
            end_pointer -= 1

        return True

