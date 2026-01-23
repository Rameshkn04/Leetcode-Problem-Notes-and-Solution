class TreeNode:
  def __init__(self, val = 0, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def distribution(self,root):
    self.moves = 0
    def dfs(node):
      if not node:
        return 0
      left = dfs(node.left)
      right = dfs(node.right)
      self.moves += abs(left) + abs(right)
      return node.val + left + right
    dfs(root)
    return self.moves
