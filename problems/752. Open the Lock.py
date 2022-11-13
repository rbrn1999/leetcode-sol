from collections import deque
class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        def wrap(state):
            return tuple((num + 10) % 10 for num in state) # in python num % 10 work the same way
        
        deadends = set([tuple(int(c) for c in deadend) for deadend in deadends])
        target = tuple(int(c) for c in target)
        
        q = deque()
        nextQ = deque()
        visited = set()
        if (0,0,0,0) in deadends:
            return -1
        q.append((0, 0, 0, 0))
        visited.add((0,0,0,0))

            
        dirs = [[0,0,0,0] for _ in range(8)]
        for i in range(4):
            dirs[i][i] = 1
            dirs[i+4][i] = -1
        dirs = [tuple(d) for d in dirs]
        stepCount = 0
        
        while q:
            state = q.popleft()
            if state == target:
                return stepCount
            for d in dirs:
                newState = map(lambda x, y: x + y, state, d)
                newState = wrap(newState)
                if newState not in visited and newState not in deadends:
                    nextQ.append(newState)
                    visited.add(newState)
            if not q:
                q, nextQ = nextQ, deque()
                stepCount += 1
        
        return -1