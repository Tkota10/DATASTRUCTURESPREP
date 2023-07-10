#Queue

from collections import deque

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def checkifadjacentzero(board, i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            return board[i][j] == 'O'

        def bfs(board, i, j):
            queue = deque([(i, j)])

            while queue:
                row, col = queue.popleft()
                if not checkifadjacentzero(board, row, col) or board[row][col] != 'O':
                    continue
                
                board[row][col] = '#'  # Mark the cell as visited

                # Enqueue neighboring cells
                queue.append((row + 1, col))
                queue.append((row - 1, col))
                queue.append((row, col + 1))
                queue.append((row, col - 1))

        # Traverse the boundaries and mark the connected 'O' cells as visited
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            bfs(board, i, 0)
            bfs(board, i, cols - 1)

        for j in range(cols):
            bfs(board, 0, j)
            bfs(board, rows - 1, j)

        # Final traversal to modify the cells
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'


#DFS

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        
        def dfs(board, i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != 'O':
                return
            
            board[i][j] = '#'  # Mark the cell as visited

            # Recursive calls for neighboring cells
            dfs(board, i + 1, j)
            dfs(board, i - 1, j)
            dfs(board, i, j + 1)
            dfs(board, i, j - 1)

        # Traverse the boundaries and mark the connected 'O' cells as visited
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            dfs(board, i, 0)
            dfs(board, i, cols - 1)

        for j in range(cols):
            dfs(board, 0, j)
            dfs(board, rows - 1, j)

        # Final traversal to modify the cells
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'




#Queue method (BFS)

from collections import deque

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def checkifadjacentzero(board, i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            return board[i][j] == 'O'

        def bfs(board, i, j):
            queue = deque([(i, j)])

            while queue:
                row, col = queue.popleft()
                if not checkifadjacentzero(board, row, col) or board[row][col] != 'O':
                    continue
                
                board[row][col] = '#'  # Mark the cell as visited

                # Enqueue neighboring cells
                queue.append((row + 1, col))
                queue.append((row - 1, col))
                queue.append((row, col + 1))
                queue.append((row, col - 1))

        # Traverse the boundaries and mark the connected 'O' cells as visited
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            bfs(board, i, 0)
            bfs(board, i, cols - 1)

        for j in range(cols):
            bfs(board, 0, j)
            bfs(board, rows - 1, j)

        # Final traversal to modify the cells
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'