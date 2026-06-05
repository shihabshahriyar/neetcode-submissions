class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        length = 0
        char_set = set()
        
        for l in range(len(s)):
            r = l
            while r < len(s) and s[r] not in char_set:
                print(s[r])
                char_set.add(s[r])
                r += 1
            length = max(length, len(char_set))
            char_set.clear()
        return length