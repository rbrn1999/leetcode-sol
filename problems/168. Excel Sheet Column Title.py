# link: https://leetcode.com/problems/excel-sheet-column-title/

from collections import deque
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        charArr = deque()
        while columnNumber > 0:
            columnNumber -= 1
            charArr.appendleft(chr((columnNumber % 26) + ord('A')))
            columnNumber //= 26
        
        return ''.join(charArr)