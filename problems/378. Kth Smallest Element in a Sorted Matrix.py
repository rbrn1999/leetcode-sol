# link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/



'''
Quick Select
Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        k -= 1
        def quickSelect(start=0, end=n*n-1):
            pivot = matrix[end // n][end % n]
            ptr = 0 # start of the right portion
            for i in range(end):
                if matrix[i // n][i % n] <= pivot:
                    matrix[ptr // n][ptr % n], matrix[i // n][i % n] = matrix[i // n][i % n], matrix[ptr // n][ptr % n] 
                    ptr += 1
            matrix[ptr // n][ptr % n], matrix[end // n][end % n] = matrix[end // n][end % n], matrix[ptr // n][ptr % n] 
            if ptr == k:
                return matrix[ptr // n][ptr % n]
            elif ptr > k:
                return quickSelect(start, ptr-1)
            else:
                return quickSelect(ptr+1, end)

        return quickSelect()