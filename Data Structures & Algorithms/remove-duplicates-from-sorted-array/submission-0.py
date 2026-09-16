class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen={*()}
        k = 0
        for i, num in enumerate(nums):
            if num not in seen:
                seen.add(num)
                nums[k] = num
                k += 1
                continue

        return k
            

