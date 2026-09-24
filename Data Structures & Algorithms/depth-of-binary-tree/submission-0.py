# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_layers = 0
        if not root:
            return 0
        def dfs(node, count = 1):
            nonlocal max_layers

            if node is None:
                return
            if count > max_layers:
                max_layers = count

            dfs(node.left, count + 1)
            dfs(node.right, count + 1)
        dfs(root)
        return max_layers
        