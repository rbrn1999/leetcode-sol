# link: https://leetcode.com/problems/smallest-number-in-infinite-set/

class SmallestInfiniteSet:

    def __init__(self):
        self.minNum = 1
        self.added = [] #[1~minNum)
        self.added_set = set()

    def popSmallest(self) -> int:
        if not self.added:
            num = self.minNum
            self.minNum += 1
        else:
            num = heapq.heappop(self.added)
            self.added_set.remove(num)

        return num

    def addBack(self, num: int) -> None:
        if num >= self.minNum or num in self.added_set:
            return

        if num == self.minNum - 1:
            self.minNum -= 1
        else:
            heapq.heappush(self.added, num)
            self.added_set.add(num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

