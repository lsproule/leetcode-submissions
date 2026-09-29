# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return (0, 0)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            rob_curr = node.val + left[1] + right[1]
            not_rob_curr = max(left) + max(right)
            
            return (rob_curr, not_rob_curr)
            
        return max(dfs(root))