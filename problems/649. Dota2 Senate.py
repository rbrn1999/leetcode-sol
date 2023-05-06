from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        Dr = deque()
        Rr = deque()
        Dl = deque()
        Rl = deque()
        for i, c in enumerate(senate):
            if c == 'D':
                Dr.append(i)
            else:
                Rr.append(i)
        while Dr or Rr:
            if Dr and (not Rr or Dr[0] < Rr[0]):
                Dl.append(Dr.popleft())
                if Rr:
                    Rr.popleft()
                elif Rl:
                    Rl.popleft()
                else:
                    return "Dire"
            else:
                Rl.append(Rr.popleft())
                if Dr:
                    Dr.popleft()
                elif Dl:
                    Dl.popleft()
                else:
                    return "Radiant"
            if not Dr and not Rr:
                if Dl and not Rl:
                    return "Dire"
                if Rl and not Dl:
                    return "Radiant"
                Dl, Dr = deque(), Dl
                Rl, Rr = deque(), Rl
        
        return "ERROR"
