class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for v in s: 
            if v in set([*"([{"]):
                stack.append(v)
                continue

            if not (len(stack) > 0): 
                return False
            val = stack.pop()

            if (v == ")" and val  !=  "("): 
               return False
            if (v == "]" and val  !=  "["):
               return False
            if (v == "}" and val  !=  "{"):
               return False
        return True if len(stack) == 0 else False

            
        