class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "D":
                val = stack.pop()
                stack.append(val)
                stack.append(val *2)
                continue
            if op == "C":
                val = stack.pop()
                continue
            if op == "+":  
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2)
                stack.append(val1)
                stack.append(val1 + val2)
                continue
            stack.append(int(op))
            print(stack)
        return sum(stack)