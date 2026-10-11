class Solution:
    def climbStairs(self, n: int) -> int:
        one_step, two_step = 1, 1
        for i in range(n-1):
            one_step, two_step = one_step + two_step, one_step
        return one_step


            
