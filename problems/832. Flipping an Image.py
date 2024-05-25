# link: https://leetcode.com/problems/flipping-an-image/t

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        n = len(image)
        for row in range(n):
            for i in range(n // 2):
                image[row][i], image[row][n-1-i] = image[row][n-1-i], image[row][i]
                image[row][i] ^= 1
                image[row][n-1-i] ^= 1
            
            if n % 2 == 1:
                image[row][n//2] ^= 1
        
        return image