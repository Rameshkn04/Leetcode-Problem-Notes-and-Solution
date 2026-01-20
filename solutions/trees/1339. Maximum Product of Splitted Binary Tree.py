# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root):
        MOD = 10**9 + 7
        self.max_product = 0
        
        # Step 1: compute total sum of tree
        def totalSumDFS(node):
            if not node:
                return 0
            return node.val + totalSumDFS(node.left) + totalSumDFS(node.right)

        total_sum = totalSumDFS(root)

        # Step 2: compute subtree sums and update max product
        def subtreeDFS(node):
            if not node:
                return 0
            
            left_sum = subtreeDFS(node.left)
            right_sum = subtreeDFS(node.right)
            subtree_sum = node.val + left_sum + right_sum
            
            # product if we split here
            self.max_product = max(
                self.max_product,
                subtree_sum * (total_sum - subtree_sum)
            )
            
            return subtree_sum

        subtreeDFS(root)
        return self.max_product % MOD
