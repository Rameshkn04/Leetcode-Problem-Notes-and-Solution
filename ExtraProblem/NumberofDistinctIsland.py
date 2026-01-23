#This question was asked in Snabbit
def numberofdistinctIsland(grid):
  n,m = len(grid), len(grid[0])
  visited = [[Flase]*m for _ in range(n)]
  shapes = set()

  def dfs(r,c, base_r, base_c, shape):
    visited[r][c] = True
    shape.append((r-base_r, c - base_c))

    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
      nc, nr = r+dr, c+dc
      if 0 <= nr < n and 0 <= nc < m:
        if grid[nr][nc] == 1 and not visited[nr][nc]:
          dfs(nr,nc,base_r,base_c, shape)

  for i in range(n):
    for j in range(m):
      if grid[i][j] == 1 and not in visited[i][j]:
        shape = []
        dfs(i,j,i,j,shape)
        shapes.add(tuple(shape))

  return len(shape)
