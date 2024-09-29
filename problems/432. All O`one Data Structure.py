# link: https://leetcode.com/problems/all-oone-data-structure/

# Doubly-Linked List

from dataclasses import dataclass
from typing import Optional

@dataclass
class Node():
    key: str
    count: int
    prev: Optional['Node'] = None
    next: Optional['Node'] = None


class AllOne:

    def __init__(self):
        self.head = Node("", 0)
        self.tail = Node("", 50000, self.head)
        self.head.next = self.tail
        self.map = {} # key: node


    def inc(self, key: str) -> None:
        if key not in self.map:
            node = Node(key, 1, self.head, self.head.next)
            self.map[key] = node
            self.head.next = node
            node.next.prev = node
        else:
            node = self.map[key]
            node.count += 1
            cur = node.next
            node.prev.next, node.next.prev = node.next, node.prev
            while cur.count < node.count:
                cur = cur.next
            prev = cur.prev
            node.prev, node.next = prev, cur
            prev.next = cur.prev = node

    def dec(self, key: str) -> None:
        node = self.map[key]
        node.count -= 1
        node.prev.next, node.next.prev = node.next, node.prev
        if node.count == 0:
            del self.map[key]
            return

        prev = node.prev
        while prev.count > node.count:
            prev = prev.prev
        next_node = prev.next
        node.prev, node.next = prev, next_node
        prev.next = next_node.prev = node


    def getMaxKey(self) -> str:
        return self.tail.prev.key

    def getMinKey(self) -> str:
        return self.head.next.key
        

# Doubly-Linked List with Freqency

from dataclasses import dataclass
from typing import Optional

@dataclass
class Node():
    key: str
    count: int
    prev: Optional['Node'] = None
    next: Optional['Node'] = None


class AllOne:

    def __init__(self):
        self.head = Node("", 0)
        self.tail = Node("", 50000, self.head)
        self.head.next = self.tail
        self.map = {} # key: node


    def inc(self, key: str) -> None:
        if key not in self.map:
            node = Node(key, 1, self.head, self.head.next)
            self.map[key] = node
            self.head.next = node
            node.next.prev = node
        else:
            node = self.map[key]
            node.count += 1
            cur = node.next
            node.prev.next, node.next.prev = node.next, node.prev
            while cur.count < node.count:
                cur = cur.next
            prev = cur.prev
            node.prev, node.next = prev, cur
            prev.next = cur.prev = node

    def dec(self, key: str) -> None:
        node = self.map[key]
        node.count -= 1
        node.prev.next, node.next.prev = node.next, node.prev
        if node.count == 0:
            del self.map[key]
            return

        prev = node.prev
        while prev.count > node.count:
            prev = prev.prev
        next_node = prev.next
        node.prev, node.next = prev, next_node
        prev.next = next_node.prev = node


    def getMaxKey(self) -> str:
        return self.tail.prev.key

    def getMinKey(self) -> str:
        return self.head.next.key
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()