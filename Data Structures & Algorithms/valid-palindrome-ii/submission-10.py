
def skipping(s:str) -> bool:
        low = 0
        high = len(s)-1
        print(s)
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True

class Solution:
    def validPalindrome(self, s: str) -> bool:
        low = 0 
        high = len(s)-1
        skipped = 0

        while low < high:
            if s[low] != s[high]:
                return bool(skipping(s[low+1:high+1]) + skipping(s[low:high]))
            low += 1
            high -= 1


        return True