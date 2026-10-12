class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        stack = []
        #res = [0] * n 

        for i in range(n-1, -1, -1):
            height = heights[i]
            visible = 0

            while stack and height > stack[-1]:
                stack.pop()
                visible += 1
            
            if stack:
                visible += 1

            heights[i] = visible

            stack.append(height)
        return heights 



