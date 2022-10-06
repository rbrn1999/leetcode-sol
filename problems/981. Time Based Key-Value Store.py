# link: https://leetcode.com/problems/time-based-key-value-store/

from collections import defaultdict
import bisect
class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        i = bisect.bisect_right(self.storage[key], (timestamp, ""))
        self.storage[key].insert(i, (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # 'z'*100 is the largest lexicographical ordered string within the constraint, we want the index to always be at the right of our target
        i = bisect.bisect_right(self.storage[key], (timestamp, 'z'*100))
        return self.storage[key][i-1][1] if i>0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
