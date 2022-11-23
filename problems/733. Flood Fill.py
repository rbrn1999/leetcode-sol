# link: https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        source_color = image[sr][sc]
        m, n = len(image), len(image[0])
        def dfs(r, c):
            if r not in range(m) or c not in range(n) or image[r][c] != source_color:
                return
            else:
                image[r][c] = color
                dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for d_r, d_c in dirs:
                    dfs(r + d_r, c + d_c)

        if source_color == color:
            return image
        else:
            dfs(sr, sc)
            return image
