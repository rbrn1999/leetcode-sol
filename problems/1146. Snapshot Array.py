# link: https://leetcode.com/problems/snapshot-array/

from bisect import bisect_left
class SnapshotArray:

    def __init__(self, length: int):
        self.snapshots = [[(-1, 0)] for _ in range(length)] # list[length]: index: [(snap_id, val)]
        self.snap_id = -1
    def set(self, index: int, val: int) -> None:
        if len(self.snapshots[index]) == 0 or self.snapshots[index][-1][0] < self.snap_id+1:
            self.snapshots[index].append((self.snap_id+1, val))
        else:
            self.snapshots[index][-1] = (self.snap_id+1, val)

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        # snap_index = bisect_left(self.snapshots[index], snap_id, key=lambda x: x[0])
        # return self.snapshots[index][snap_index][1]
        # binary search
        low = 0
        high = len(self.snapshots[index])-1
        while low+1 < high:
            mid = (low + high) // 2
            if self.snapshots[index][mid][0] > snap_id:
                high = mid-1
            elif self.snapshots[index][mid][0] < snap_id:
                low = mid
            else:
                return self.snapshots[index][mid][1]
        return self.snapshots[index][low][1] if self.snapshots[index][high][0] > snap_id else self.snapshots[index][high][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
