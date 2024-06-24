# link: https://leetcode.com/problems/grumpy-bookstore-owner/

class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        n = len(customers)
        increased_customers = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                increased_customers += customers[i]

        max_increased_customers = increased_customers
        for i in range(minutes, n):
            if grumpy[i-minutes] == 1:
                increased_customers -= customers[i-minutes]
            if grumpy[i] == 1:
                increased_customers += customers[i]

            max_increased_customers = max(max_increased_customers, increased_customers)

        return sum(customers[i] for i in range(n) if grumpy[i] == 0) + max_increased_customers
