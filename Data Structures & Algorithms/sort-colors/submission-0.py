class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red = white = blue = -1
        for i in range(len(nums)):
            x = nums[i]
            blue += 1
            if x == 2:
                nums[blue] = 2
                continue
    
            white += 1
            if white != blue:
                nums[blue] = 2
            if x == 1:
                nums[white] = 1
                continue
    
            red += 1
            if red != white:
                nums[white] = 1
            nums[red] = 0