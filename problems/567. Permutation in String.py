# link: https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26

        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        for i in range(n):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        if count1 == count2:
            return True

        for i in range(n, m):
            count2[ord(s2[i]) - ord('a')] += 1
            count2[ord(s2[i-n]) - ord('a')] -= 1
            if count1 == count2:
                return True

        return False

