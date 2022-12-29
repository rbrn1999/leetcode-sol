# link: https://leetcode.com/problems/search-a-2d-matrix/

from typing import List

# 2022/12/29, time complexity: O(log(m)+log(n))
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        start = 0
        end = ROWS-1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if matrix[mid][0] <= target:
                start = mid
            else:
                end = mid - 1
        
        
        row = end if matrix[end][0] <= target else start
        
        start = 0
        end = COLS - 1
        while start <= end:
            mid = start + (end - start) // 2
            if matrix[row][mid] < target:
                start = mid + 1
            elif matrix[row][mid] > target:
                end = mid - 1
            else:
                return True
        
        return False
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