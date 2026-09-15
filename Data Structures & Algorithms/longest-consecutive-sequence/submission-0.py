


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        seen = set()

        for num in nums:
            seen.add(num)

        for num in seen: 
            if num -1 in seen:
                continue

            count = 1
            i =  num + 1
            while i in seen:
                i += 1
                count+=1
            if count > max_count:
                max_count = count

        return max_count 
