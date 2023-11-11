class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        max_len = 0
        left = 0

        for i in range(len(s)):
            while s[i] in seen:
                seen.pop(0)
                left += 1

            seen.append(s[i])
            max_len = max(max_len, i - left + 1)

        return max_len
