# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            # Max contribution from left and right subtrees
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))
            
            # Path passing through this node
            current_path = node.val + left_gain + right_gain
            
            # Update global maximum
            self.max_sum = max(self.max_sum, current_path)
            
            # Return max path extending to parent
            return node.val + max(left_gain, right_gain)
        
        dfs(root)
        return self.max_sum

        
