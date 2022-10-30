# link: https://leetcode.com/problems/image-overlap/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        m, n = len(img1), len(img1[0])
        res = 0
        def compare(xOff, yOff):
            count = 0
            yRange = range(m-yOff) if yOff >= 0 else range(-yOff, m)
            xRange = range(n-xOff) if xOff >= 0 else range(-xOff, n)
            for i in yRange:
                for j in xRange:
                    if img1[i][j] == 1 and img2[i+yOff][j+xOff] == 1:
                        count += 1

            nonlocal res
            res = max(res, count)

        for i in range(-m, m):
            for j in range(-n, n):
                if res >= (m-i)*(n-j):
                    break
                compare(j, i)
        return res

