# link: https://leetcode.com/problems/online-stock-span/

'''
solution reference: https://leetcode.com/problems/online-stock-span/solution
Time Complexity: O(1)
Space Complexity: O(n)
n: number of calls
'''
class StockSpanner:

    def __init__(self):
        self.stack = []
    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res

'''
Time Complexity: O(n)
Space Complexity: O(n)
n: number of calls
'''
class StockSpanner:

    def __init__(self):
        self.prices = []
        self.start = 0
    def next(self, price: int) -> int:
        if not self.prices or price < self.prices[-1]:
            self.prices.append(price)
            self.start = len(self.prices) - 1
            return 1
        while self.start >= 0 and self.prices[self.start] <= price:
            self.start -= 1
        self.start += 1
        self.prices.append(price)
        return len(self.prices) - self.start




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
