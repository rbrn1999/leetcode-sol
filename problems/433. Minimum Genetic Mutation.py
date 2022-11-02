# link: https://leetcode.com/problems/minimum-genetic-mutation/

from collections import deque
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        chrs = set(['A', 'C', 'G', 'T'])
        bank = set(bank)
        seen = set()

        cur = deque([start])
        nxt = deque()
        count = 0

        if end not in bank:
            return -1

        while cur:
            s = cur.popleft()
            if s == end:
                return count
            for i in range(8):
                for c in chrs - set([s[i]]):
                    nS = s[:i] + c + s[i+1:]
                    if nS not in seen and nS in bank:
                        seen.add(nS)
                        nxt.append(nS)

            if not cur:
                cur, nxt = nxt, deque()
                count += 1

        return -1
