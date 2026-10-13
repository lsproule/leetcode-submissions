class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(index, subset = None): 
            if subset is None:
                subset = []
            if len(nums) == index:
                return res.append(subset[:])
            
            dfs(index + 1, subset[:])
            subset.append(nums[index])
            dfs(index+1, subset[:])
        dfs(0)
        return res
        