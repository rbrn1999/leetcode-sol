class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        #return max([sum(customer) for customer in accounts])

        #faster
        return max(map(sum, accounts))