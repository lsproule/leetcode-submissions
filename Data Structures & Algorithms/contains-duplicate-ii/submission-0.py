class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = [] 
        for i, num  in enumerate(nums):
            if num in seen:
                return True
            seen.append(num)
            if len(seen) > k:
                seen.pop(0)
        return False
                
    