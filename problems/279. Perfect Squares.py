import bisect
from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i ** 2 <= n:
            squares.append(i ** 2)
            i += 1
        if squares[-1] == n:
            return 1
        
        curStep = deque([n - square for square in squares[::-1]])
        nxtStep = deque()
        
        stepCount = 1
        while curStep:
            remain = curStep.popleft()
            maxInd = bisect.bisect_right(squares, remain) - 1
            for i in range(maxInd, -1, -1):
                if squares[i] < remain:
                    nxtStep.append(remain - squares[i])
                elif squares[i] == remain:
                    return stepCount + 1
            
            if not curStep:
                curStep, nxtStep = nxtStep, deque()
                stepCount += 1
        
        return float('inf')
        