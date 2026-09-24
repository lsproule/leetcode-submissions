# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        seen = {*()} 
        visited = []
        def dfs(node, seen):
            if  node is None or node.val in seen:
                return

            print(node.val)
            if node.left is None or node.left.val in seen:
                visited.append(node.val)
                seen.add(node.val)
                dfs(node.right, seen)
                return
            if node.left is not None and node.left.val not in seen:
                dfs(node.left, seen)
                dfs(node, seen)
                


        dfs(root, seen)
        return visited