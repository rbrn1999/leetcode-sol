# link: https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

# 3D DP
class Solution:
    def longestLine(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        answer = 0

        dp = [[[0] * (4) for _ in range(n+2)] for _ in range(m+1)]
        # pad one row and one left col and one right col
        # 0: row, 1: col, 2: dig, 3: anti-diag

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    continue
                dp[r+1][c+1][0] = dp[r+1][c][0] + 1
                dp[r+1][c+1][1] = dp[r][c+1][1] + 1
                dp[r+1][c+1][2] = dp[r][c][2] + 1
                dp[r+1][c+1][3] = dp[r][c+2][3] + 1
                answer = max(answer, max(dp[r+1][c+1]))

        return answer

# 2D DP
class Solution:
    def longestLine(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        answer = 0

        dp = [[[0] * 4 for _ in range(n+2)] for _ in range(2)]
        # 0: row, 1: col, 2: dig, 3: anti-diag

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    continue
                dp[1][c+1][0] = dp[1][c][0] + 1
                dp[1][c+1][1] = dp[0][c+1][1] + 1
                dp[1][c+1][2] = dp[0][c][2] + 1
                dp[1][c+1][3] = dp[0][c+2][3] + 1
                answer = max(answer, max(dp[1][c+1]))

            dp = [dp[1], [[0] * 4 for _ in range(n+2)]]

        return answer


# Brute Force
class Solution:
    def longestLine(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        answer = 0

        # row
        for row in range(m):
            ones = 0
            for col in range(n):
                if mat[row][col] == 1:
                    ones += 1
                else:
                    answer = max(answer, ones)
                    ones = 0

            answer = max(answer, ones)

        # col
        for col in range(n):
            ones = 0
            for row in range(m):
                if mat[row][col] == 1:
                    ones += 1
                else:
                    answer = max(answer, ones)
                    ones = 0

            answer = max(answer, ones)


        # lower diag (mid to bottom-left)
        for row in range(m):
            col = 0
            ones = 0
            while row < m and col < n:
                if mat[row][col] == 1:
                    ones += 1
                else:
                    answer = max(answer, ones)
                    ones = 0

                row += 1
                col += 1

            answer = max(answer, ones)

        # upper diag (mid to top-right)
        for col in range(n):
            row = 0
            ones = 0
            while row < m and col < n:
                if mat[row][col] == 1:
                    ones += 1
                else:
                    answer = max(answer, ones)
                    ones = 0

                row += 1
                col += 1

            answer = max(answer, ones)

        # lower anti-diag (mid to top-left)
        for row in range(m):
            col = 0
            ones = 0
            while row >= 0 and col < n:
                if mat[row][col] == 1:
                    ones += 1
                else:
                    answer = max(answer, ones)
                    ones = 0

                row -= 1
                col += 1

            answer = max(answer, ones)

        # lower diag (mid to bottom-right)
        for col in range(n):
            row = m - 1
            ones = 0
            while row >= 0 and col < n:
                if mat[row][col] == 1:
                    ones += 1
                else:
                    answer = max(answer, ones)
                    ones = 0

                row -= 1
                col += 1

            answer = max(answer, ones)

        return answer
