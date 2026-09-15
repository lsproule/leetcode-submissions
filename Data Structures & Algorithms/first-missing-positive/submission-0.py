class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        solution = set(nums)
        i = 1
        
        while i in solution:  
            i += 1
        return i