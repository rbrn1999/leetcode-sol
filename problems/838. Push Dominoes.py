# link: https://leetcode.com/problems/push-dominoes/

from collections import deque
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = [c for c in dominoes]
        n = len(dominoes)
        processed = set()
        q = deque()
        for i, state in enumerate(dominoes):
            if state != '.':
                processed.add(i)
                q.append(i)

        while q:
            processed.update(q)
            for _ in range(len(q)):
                i = q.popleft()
                if dominoes[i] == 'R' and i < n-1:
                    if (i+1) in processed:
                        continue
                    elif dominoes[i+1] == '.':
                        dominoes[i+1] = 'R'
                        q.append(i+1)
                    else:
                        dominoes[i+1] = '.'
                if dominoes[i] == 'L' and i > 0:
                    if (i-1) in processed:
                        continue
                    if dominoes[i-1] == '.':
                        dominoes[i-1] = 'L'
                        q.append(i-1)
                    else:
                        dominoes[i-1] = '.'
        
        return ''.join(dominoes)
