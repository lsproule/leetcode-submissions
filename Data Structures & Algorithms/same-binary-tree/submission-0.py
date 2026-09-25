# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p_node, q_node):
            if p_node is None and q_node is None:
                return True

            if p_node is None or q_node is None:
                return False

            print(q_node.val, p_node.val)
            if q_node.val != p_node.val:
                return False
            return dfs(p_node.left, q_node.left) and dfs(p_node.right, q_node.right)


        return dfs(p, q)
        