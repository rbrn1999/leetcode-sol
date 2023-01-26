# link: https://leetcode.com/problems/snakes-and-ladders/

from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        ROW, COL = len(board), len(board[0])
        def numberToPosition(number):
            number -= 1
            row = (ROW - 1) - (number // COL)
            col = (number % COL) if ((ROW - 1) - row) % 2 == 0 else (COL - 1 - (number % COL))
            return (row, col)
        def positionToNumber(row, col):
            rowCount = (ROW-1) - row
            number = rowCount * COL + (col % COL if rowCount % 2 == 0 else (COL - 1 - col % COL) + 1)
            return number

        steps = 0
        queue = deque()
        queue.append(1)
        visited = set()

        # BFS
        while queue:
            size = len(queue)
            for _ in range(size):
                number = queue.popleft()
                for newNum in range(number+1, min(number+6, ROW*COL) + 1):
                    newNumNoWarp = newNum
                    if newNum in visited:
                        continue
                    if newNum == ROW * COL:
                        return steps + 1
                    row, col = numberToPosition(newNum)
                    visited.add(newNum)
                    if board[row][col] != -1:
                        newNum = board[row][col]
                        row, col = numberToPosition(newNum)
                        if newNum == ROW * COL:
                            return steps + 1
                        # add to visited if there's a ladder/snake but we can't take it
                        if board[row][col] == -1:
                            visited.add(newNum)

                    queue.append(newNum)
            steps += 1

        return -1
