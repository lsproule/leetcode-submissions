class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
               

        return max(counter, key=counter.get)