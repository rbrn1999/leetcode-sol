# link: https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix[0])
        for i in range(N // 2):
            for j in range(i, N - i - 1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[N - 1 - j][i]
                matrix[N - 1 - j][i] = matrix[N - 1 - i][N - 1 - j]
                matrix[N - 1 - i][N - 1 - j] = matrix[j][N - 1 - i]
                matrix[j][N - 1 - i] = temp


# solution reference: https://youtu.be/fMSJSS7eO1w
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        low, high = 0, len(matrix) - 1
        while low < high:
            top = left = low
            bottom = right = high
            for i in range(high-low):
                topLeft = matrix[top][left+i]
                # move bottom left into top left
                matrix[top][left+i] = matrix[bottom-i][left]
                # move bottom right into bottom left
                matrix[bottom-i][left] = matrix[bottom][right-i]
                # move top right into bottom right
                matrix[bottom][right-i] = matrix[top+i][right]
                # move top left into top right
                matrix[top+i][right] = topLeft
            high -= 1
            low += 1

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        # reverse and transpose (double flip)
        # transpose is like a diagnol flip
        # reverse
        matrix.reverse()
        
        # transpose
        for i in range(n):
            for j in range(i):
                print(matrix[i][j])
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        