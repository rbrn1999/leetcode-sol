# link: https://leetcode.com/problems/student-attendance-record-ii/

class Solution:
    def checkRecord(self, n: int) -> int:
        memo = [[0] * 3 for _ in range(2)] # absense, late streak
        memo[0][0] = 1
        for _ in range(n):
            temp = [[0] * 3 for _ in range(2)]
            temp[0][0] = sum(memo[0]) % int(1E9 + 7)
            temp[0][1] = memo[0][0] % int(1E9 + 7)
            temp[0][2] = memo[0][1] % int(1E9 + 7)
            temp[1][0] = (sum(memo[0]) + sum(memo[1])) % int(1E9 + 7)
            temp[1][1] = memo[1][0] % int(1E9 + 7)
            temp[1][2] = memo[1][1] % int(1E9 + 7)
            memo = temp

        return sum(sum(l) for l in memo) % int(1E9 + 7)

