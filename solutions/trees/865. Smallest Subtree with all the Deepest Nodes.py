# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root):
        
        def dfs(node):
            if not node:
                return (0, None)
            
            leftDepth, leftNode = dfs(node.left)
            rightDepth, rightNode = dfs(node.right)
            
            if leftDepth > rightDepth:
                return (leftDepth + 1, leftNode)
            if rightDepth > leftDepth:
                return (rightDepth + 1, rightNode)
            
            # Equal depth → current node is LCA
            return (leftDepth + 1, node)
        
        return dfs(root)[1]

        
