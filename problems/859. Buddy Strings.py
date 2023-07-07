# link: https://leetcode.com/problems/buddy-strings/

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)

        c1, c2 = "", ""
        g1, g2 = "", ""

        for i in range(len(s)):
            if s[i] == goal[i]:
                continue
            if not c1:
                c1 = s[i]
                g1 = goal[i]
            elif not c2:
                c2 = s[i]
                g2 = goal[i]
            else:
                return False

        return c1 == g2 and c2 == g1

