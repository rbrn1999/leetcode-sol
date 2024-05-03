# link: https://leetcode.com/problems/rle-iterator/

class RLEIterator:

    def __init__(self, encoding: list[int]):
        self.stack = list(reversed(encoding))

    def next(self, n: int) -> int:
        if self.stack and self.stack[-1] == 0:
            self.stack.pop()
            self.stack.pop()

        while self.stack and n > self.stack[-1]:
            n -= self.stack.pop()
            self.stack.pop()

        if not self.stack:
            return -1

        self.stack[-1] -= n
        return self.stack[-2]


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
