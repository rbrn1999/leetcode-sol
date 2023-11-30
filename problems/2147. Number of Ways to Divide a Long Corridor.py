# link: https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

# DP
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seat_combs = [1] + [0] * 2
        for c in corridor:
            next_combs = [0] * 3
            if c == 'P':
                next_combs[0] = (seat_combs[0] + seat_combs[2]) % (10 ** 9 + 7)
                next_combs[1] = seat_combs[1]
                next_combs[2] = seat_combs[2]
            else:
                next_combs[0] = 0
                next_combs[1] = (seat_combs[0] + seat_combs[2]) % (10 ** 9 + 7)
                next_combs[2] = seat_combs[1]
            
            seat_combs = next_combs
        
        return seat_combs[2]

# Math
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats = 0
        plants = 0
        ans = 1
        for c in corridor:
            if seats < 2:
                if c == 'S':
                    seats += 1
            else:
                if c == 'S':
                    ans *= (plants + 1)
                    ans %= (10**9 + 7)
                    seats = 1
                    plants = 0
                else:
                    plants += 1

        return ans if seats == 2 else 0