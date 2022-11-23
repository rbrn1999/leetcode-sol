# link: https://leetcode.com/problems/implement-stack-using-queues/

from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        res = self.q1.pop()
        self.q1, self.q2 = self.q2, self.q1
        return res
    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        res = self.q1[0]
        self.q2.append(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1
        return res

    def empty(self) -> bool:
        return not self.q1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


#follow-up: using 1 queue only
from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        n = len(self.q)
        for _ in range(n-1):
            self.q.append(self.q.popleft())
        return self.q.popleft()
    def top(self) -> int:
        n = len(self.q)
        for _ in range(n-1):
            self.q.append(self.q.popleft())
        res = self.q.popleft()
        self.q.append(res)
        return res

    def empty(self) -> bool:
        return not self.q
