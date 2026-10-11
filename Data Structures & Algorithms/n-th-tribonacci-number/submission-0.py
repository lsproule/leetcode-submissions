class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b, c = 1, 1
        if n < 3:
            return [a, b, c][n]

        for i in range(n):
            a, b, c = b, c, a+b+c
        

        return a
