# link: https://leetcode.com/problems/calculate-money-in-leetcode-bank/

class Solution:
    def totalMoney(self, n: int) -> int:
        week = n // 7
        first_week = (1 + 7) * 7 // 2
        last_week = first_week + 7 * (week - 1)
        full_week_amount = week * (first_week + last_week) // 2
        remain = ((week + 1) + (week + n % 7)) * (n % 7) // 2
        return full_week_amount + remain