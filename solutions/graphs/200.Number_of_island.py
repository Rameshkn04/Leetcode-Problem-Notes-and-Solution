class Solution:
  def graph(self, grid):
    if not grid:
      return 0
    rows,cols = len(grid), len(grid[0])
    visited = set()
    island = 0
    
    def dfs(r,c):
      if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0' or (r,c) in visited):
        return
      visited.add((r,c))
      #visit all four neighbours
      dfs(r+1,c) #down
      dfs(r-1,c) #up
      dfs(r,c+1) #right
      dfs(r,c-1) #left
    #Traverse the grid
    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == '1' and (r,c) not in visited:
          dfs(r,c)
          island += 1
    return island


#Most important queston it was asked in Snabbit Exam must practise this question daily 

