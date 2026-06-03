class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R  = 0, len(s) - 1
        s = s.lower()

        while L < R:
            while s[L].isalnum() == False and L < R:
                L += 1
            while s[R].isalnum() == False and R > L:
                R -= 1

            if s[L] != s[R]:
                return False
            
            L += 1
            R -= 1
        
        return True