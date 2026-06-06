class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        maxLength = 0
        l = 0
        for r in range(len(s)):
            count[ord(s[r]) - 65] += 1
            if (r-l) + 1 - max(count) > k:
                count[ord(s[l]) - 65] -= 1
                l += 1

            maxLength = max(maxLength, (r-l) + 1)

        return maxLength
                