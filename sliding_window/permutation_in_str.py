class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = [0] * 26
        s2_counter = [0] * 26
        for char in s1:
            index = ord(char) - ord("a")
            s1_counter[index] += 1

        l = 0
        for i, char in enumerate(s2):
            index = ord(char) - ord("a")
            s2_counter[index] += 1

            while i - l + 1 > len(s1):
                index = ord(s2[l]) - ord("a")
                s2_counter[index] -= 1
                l += 1

            if i - l + 1 == len(s1):
                if s1_counter == s2_counter:
                    return True

        return False
