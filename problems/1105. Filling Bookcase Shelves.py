# link: https://leetcode.com/problems/filling-bookcase-shelves/

# Recursion + Memoization

from functools import cache
class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        @cache
        def helper(i: int, width: int, rowHeight: int) -> int:
            if i == len(books):
                return rowHeight

            sameRow = float('inf')
            nextRow = rowHeight + helper(i+1, shelfWidth-books[i][0], books[i][1])
            if books[i][0] <= width:
                sameRow = helper(i+1, width-books[i][0], max(rowHeight, books[i][1]))

            return min(sameRow, nextRow)

        return helper(0, shelfWidth, 0)


# Bottom-Up

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        # dp[i]: min height for the first i books placed on the shelf
        dp = [0] + [float('inf')] * n

        for i in range(1, n+1):
            max_width = shelfWidth
            row_height = 0
            j = i-1

            # place [j, i] books on the same row
            while j >= 0 and max_width >= books[j][0]:
                max_width -= books[j][0]
                row_height = max(row_height, books[j][1])
                dp[i] = min(dp[i], dp[j] + row_height)
                j -= 1

        return dp[n]
