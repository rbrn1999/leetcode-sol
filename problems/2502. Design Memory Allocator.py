# link: https://leetcode.com/problems/design-memory-allocator/

from collections import defaultdict
class Allocator:

    def __init__(self, n: int):
        self.memo = [0] * n
        self.mIDMap = defaultdict(list)
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        count = 0
        start = -1
        for i in range(self.n):
            if self.memo[i] != 0:
                count = 0
            else:
                count += 1
                if count == size:
                    start = i - (size-1)
                    break
        if start > -1:
            for i in range(start, start+size):
                self.memo[i] = mID
                self.mIDMap[mID].append(i)
        return start

    def free(self, mID: int) -> int:
        size = len(self.mIDMap[mID])
        for i in self.mIDMap[mID]:
            self.memo[i] = 0
        del self.mIDMap[mID]
        return size


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
