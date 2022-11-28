# link: https://leetcode.com/problems/minimum-penalty-for-a-shop/

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        cur = customers.count('Y')
        res = (0, cur)
        for i in range(1, n+1):
            if customers[i-1] == 'Y':
                cur -= 1
                if cur < res[1]:
                    res = (i, cur)
            else:
                cur += 1

        return res[0]

