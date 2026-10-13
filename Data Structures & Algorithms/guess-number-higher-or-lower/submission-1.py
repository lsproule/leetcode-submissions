# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        high= (2**31)
        low = 1
        g = -1 
        while g != 0: 
            current_guess = (high +  low) // 2
            g = guess(current_guess)
            if g == -1:
                high = current_guess
            if g == 1:
                low = current_guess
        return current_guess
            
      
