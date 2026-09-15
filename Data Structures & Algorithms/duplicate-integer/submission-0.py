class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visto = set()
        for num in nums:
            if num in visto:
                return True
            visto.add(num)
        return False

         