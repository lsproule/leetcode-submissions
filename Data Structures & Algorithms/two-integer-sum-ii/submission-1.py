class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums)-1

        while low < high:
            if nums[low] + nums[high] == target:
                return [low+1, high +1]
            if nums[low] + nums[high] > target:
                high -= 1
            if nums[low] + nums[high] < target:
                low += 1       
        return -1