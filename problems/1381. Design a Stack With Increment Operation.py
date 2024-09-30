# link: https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.increments = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        else:
            i = len(self.stack) - 1
            value = self.stack.pop()
            value += self.increments[i]
            if i > 0:
                self.increments[i-1] += self.increments[i]
            self.increments[i] = 0
            return value

    def increment(self, k: int, val: int) -> None:
        k = min(k, len(self.stack)) - 1
        if k < 0:
            return

        self.increments[k] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
