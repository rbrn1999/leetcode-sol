class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        graph = [[[0, 0] for _ in  range(n)] for _ in range(m)]
        def backtrack(row, col, isAlantic):
            graph_ind = int(isAlantic)
            graph[row][col][graph_ind] = 1
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for offset_r, offset_c in directions:
                i, j = row + offset_r, col + offset_c
                if i < 0 or j < 0 or i >= m or j >= n or \
                    heights[i][j] < heights[row][col] or graph[i][j][graph_ind] == 1:
                    continue
                backtrack(i, j, isAlantic)
        
        for i in range(n):
            backtrack(0, i, False)
            backtrack(m-1, i, True)
        for i in range(m):
            backtrack(i, 0, False)
            backtrack(i, n-1, True)
        
        for row in graph:
            print(row)
        res = []
        for i in range(m):
            for j in range(n):
                if graph[i][j] == [1, 1]:
                    res.append([i, j])
        
        return res
  