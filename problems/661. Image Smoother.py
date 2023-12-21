# link: https://leetcode.com/problems/image-smoother/

class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        m, n = len(img), len(img[0])

        for row in range(m):
            for col in range(n):
                val = 0
                count = 0
                for r in range(max(row-1, 0), min(row+2, m)):
                    for c in range(max(col-1, 0), min(col+2, n)):
                        count += 1
                        val += img[r][c] % 256
                img[row][col] = img[row][col] | (val // count) << 8
                
        for row in range(m):
            for col in range(n):
                img[row][col] >>= 8

        return img