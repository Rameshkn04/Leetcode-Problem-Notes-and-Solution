# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # Definition for a binary tree node.
        if n == 0:
            return []
        memo = {}
        def build(start,end):
            if start > end:
                return [None]
            all_tree = []
            if (start,end) in memo:
                return memo[(start,end)]
            for root_val in range(start,end+1):
                left_tree = build(start,root_val - 1)
                right_tree = build(root_val+1,end)
                for left in left_tree:
                    for right in right_tree:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        all_tree.append(root)
            memo[(start,end)] = all_tree
            return all_tree
        return build(1,n)
