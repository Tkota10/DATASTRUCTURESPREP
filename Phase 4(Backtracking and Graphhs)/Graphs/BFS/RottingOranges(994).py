from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        fresh_count = 0
        queue = deque()

        # Count fresh oranges and initialize the queue with initial rotten oranges
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue and fresh_count > 0:
            
            for i in range(len(queue)):
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if (nx < 0 or nx == len(grid) or
                        ny < 0 or ny == len(grid[0]) or
                        grid[nx][ny] != 1):
                        continue
                    grid[nx][ny] = 2  # Mark the fresh orange as rotten
                    fresh_count -= 1
                    queue.append((nx, ny))

            minutes += 1

        return minutes if fresh_count == 0 else -1