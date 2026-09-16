class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        arr_len = len(nums)
        left = 0
        right = 0
        while right < arr_len:
            nums[left] = nums[right]
            while right < arr_len and nums[right] == nums[left]:
                right += 1
            left += 1
        return left