import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        lo = 0 
        hi = len(s)-1
        while lo < hi:
            if s[lo].isspace() or not s[lo].isalnum():
                lo +=1
                continue
            if s[hi].isspace() or not s[hi].isalnum():
                hi -=1
                continue
            if s[lo].lower() != s[hi].lower():
                print(s[lo], s[hi])
                return False
            lo +=  1
            hi -= 1
        return True