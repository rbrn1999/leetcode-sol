# link: https://leetcode.com/problems/total-distance-traveled/

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        result = 0
        r = 0
        while mainTank > 0:
            result += mainTank * 10
            q, r = min((mainTank+r) // 5, additionalTank), (mainTank+r) % 5
            additionalTank -= q
            mainTank = q

        return result

# optimal solution
def distanceTraveled(self, a: int, b: int) -> int:
        return (a + min((a - 1) // 4, b)) * 10

