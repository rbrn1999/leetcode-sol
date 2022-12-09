# link: https://leetcode.com/problems/insert-delete-getrandom-o1/
# solution referrence: https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/455253

import random
class RandomizedSet:

    def __init__(self):
        self.s = dict() # item: index
        self.l = list()
        self.length = 0

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        else:
            self.s[val] = self.length # last index value
            self.l.append(val)
            self.length += 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.s:
            return False
        else:
            # swap element to be delete with the last element
            self.s[self.l[-1]] = self.s[val]
            self.l[self.s[val]] = self.l[-1]
            del self.s[val]
            del self.l[-1]
            self.length -= 1
            return True

    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
