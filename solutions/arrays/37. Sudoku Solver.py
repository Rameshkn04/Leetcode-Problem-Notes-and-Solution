class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == '.':
                    empties.append((i, j))
                else:
                    rows[i].add(ch)
                    cols[j].add(ch)
                    boxes[(i // 3) * 3 + (j // 3)].add(ch)

        def backtrack(idx):
            if idx == len(empties):
                return True  # Solved

            r, c = empties[idx]
            box = (r // 3) * 3 + (c // 3)

            for ch in map(str, range(1, 10)):
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[box]:
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[box].add(ch)

                    if backtrack(idx + 1):
                        return True

                    board[r][c] = '.'
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[box].remove(ch)

            return False

        backtrack(0)
        
                    
