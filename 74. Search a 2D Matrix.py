# link: https://leetcode.com/problems/search-a-2d-matrix/

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        def bSearch(start, end):
            
            if start > end:
                return False
            
            mid = (start + end) // 2
            val = matrix[mid // n][mid%n]
            
            if val == target:
                return True
            elif val < target:
                return bSearch(mid+1, end)
            else:
                return bSearch(start, mid-1)
            
        
        return bSearch(0, m*n-1)

output = Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)
print(output)