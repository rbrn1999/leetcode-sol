# link: https://leetcode.com/problems/find-the-winner-of-the-circular-game/

# Simulation
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1, n+1))
        current = 0
        for _ in range(len(players)-1):
            current = (current + k - 1) % len(players)
            players.pop(current)
            current %= len(players)

        return players.pop()
# Recursion
class Solution:
    def helper(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        return (self.helper(n-1, k) + k) % n

    def findTheWinner(self, n: int, k: int) -> int:
        return self.helper(n, k) + 1

# Iterative
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        result = 0
        for i in range(2, n+1):
            result = (result + k) % i

        return result + 1
