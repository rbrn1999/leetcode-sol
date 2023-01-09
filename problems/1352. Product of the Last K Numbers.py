# link: https://leetcode.com/problems/product-of-the-last-k-numbers/

class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(num*self.prefix[-1])

    def getProduct(self, k: int) -> int:
        if len(self.prefix) <= k: # there [1] padding at the start
            return 0
        return self.prefix[-1]//self.prefix[-k-1]



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
