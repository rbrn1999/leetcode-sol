# link: https://leetcode.com/problems/largest-3-same-digit-number-in-string/

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        candidate = -1
        streak = 0
        for i, n in enumerate(num):
            if n != num[i-1]:
                streak = 1
            elif streak == 2:
                candidate = max(int(n), candidate)
                streak = 0
            else:
                streak += 1
        
        return str(candidate) * 3 if candidate > -1 else ""