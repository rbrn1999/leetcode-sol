# link: https://leetcode.com/problems/finding-mk-average/

from sortedcontainers import SortedList
from collections import deque
class MKAverage:

    def __init__(self, m: int, k: int):
        self.nums = SortedList()
        self.q = deque()
        self.m = m
        self.k = k
        self.total = self.first_k = self.last_k = 0

    def addElement(self, num: int) -> None:
        self.total += num
        self.q.append(num)
        index = self.nums.bisect_left(num)

        if index < self.k:
            self.first_k += num
            if len(self.nums) >= self.k:
                self.first_k -= self.nums[self.k - 1]

        if index >= len(self.nums) + 1 - self.k:
            self.last_k += num
            if len(self.nums) >= self.k:
                self.last_k -= self.nums[-self.k]

        self.nums.add(num)
        if len(self.q) > self.m:
            num = self.q.popleft()
            self.total -= num
            index = self.nums.index(num)
            if index < self.k:
                self.first_k -= num
                self.first_k += self.nums[self.k]
            elif index >= len(self.nums) - self.k:
                self.last_k -= num
                self.last_k += self.nums[-self.k - 1]

            self.nums.remove(num)
            
    def calculateMKAverage(self) -> int:
        if len(self.q) < self.m:
            return -1
        else:
            return (self.total - self.first_k - self.last_k) // (self.m - 2 * self.k)
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()