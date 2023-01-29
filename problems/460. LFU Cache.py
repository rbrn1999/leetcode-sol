# link: https://leetcode.com/problems/lfu-cache/

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.map = {}
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self._remove(self.map[key])
        self._insert(self.map[key])
        return self.map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(self.map[key])
        else:
            self.size += 1
        self.map[key] = Node(key, value)
        self._insert(self.map[key])
        if self.size > self.capacity:
            del self.map[self.left.next.key]
            self._remove(self.left.next)
            self.size -= 1

    def _insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next, node.prev = node, prev
        node.next, nxt.prev = nxt, node

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

