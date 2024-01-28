class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        rows, cols = len(grid), len(grid[0])
        minutes = 0
        queue = deque()
        visited = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j,0))

        while len(queue) > 0:
            (i, j, k) = queue.popleft()
            if (i,j) in visited:
                continue
            visited.add((i,j))
            for di in directions:
                ni, nj = i + di[0], j + di[1]
                if (ni >= 0 and ni < rows) and (nj >= 0 and nj < cols):
                    if (ni, nj) not in visited and grid[ni][nj] == 1:
                        minutes = max(minutes, k+1)
                        grid[ni][nj] = 2
                        queue.append((ni, nj, k+1))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        
        return minutes
