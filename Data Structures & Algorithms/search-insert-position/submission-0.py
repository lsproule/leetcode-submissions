class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        if target  < nums[low]:
            return 0

        if target > nums[high]:
            return high + 1

        while target > nums[low] or target < nums[high] and low != high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
                continue
            else:
                high = mid - 1

        return low