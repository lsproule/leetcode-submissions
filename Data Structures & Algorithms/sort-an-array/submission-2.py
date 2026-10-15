import random
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def qs(lo: int, hi: int) -> None:
            while lo < hi:
                p = nums[random.randint(lo, hi)]
                lt, i, gt = lo, lo, hi
                while i <= gt:
                    if nums[i] < p:
                        nums[lt], nums[i] = nums[i], nums[lt]
                        lt += 1
                        i += 1
                    elif nums[i] > p:
                        nums[i], nums[gt] = nums[gt], nums[i]
                        gt -= 1
                    else:
                        i += 1
                if lt - lo < hi - gt:
                    qs(lo, lt - 1)
                    lo = gt + 1
                else:
                    qs(gt + 1, hi)
                    hi = lt - 1

        qs(0, len(nums) - 1)
        return nums