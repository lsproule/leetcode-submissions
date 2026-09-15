class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []        
        for log in logs:
            if log == "./":
                continue
            if log == "../":
                if len(stack) >= 1:
                    stack.pop()
                continue
            stack.append(log)
        return len(stack)