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
           if (start,end) in memo:
             return memo[(start,end)]
           all_trees = []
           for root_val in range(start,end+1):
             left_trees = build(start, root_val-1)
             right_trees = build(root_val+1, end)
             for left in left_trees:
               for right in right_trees:
                 root = TreeNode
                 root.left = left
                 root.right = right
                 all_trees.append(root)
               memo[(start,end)] = all_trees
               return all_trees
            return build(1,n)  
'''
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]
'''
