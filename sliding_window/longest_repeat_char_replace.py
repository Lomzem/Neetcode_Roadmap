class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we want to get the longest substring where there are k-1 duplicates?
        left = 0
        seen = {}
        max_len = 0

        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1

            while i - left + 1 - max(seen.values()) > k:
                seen[s[left]] = seen.get(s[left], 0) - 1
                left += 1

            max_len = max(max_len, i - left + 1)

        return max_len
