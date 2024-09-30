# link: https://leetcode.com/problems/design-circular-deque/


# Linked List
from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    value: int = 0
    next: Optional['Node'] = None
    prev: Optional['Node'] = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        node = Node(value, self.head.next, self.head)
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        node = Node(value, self.tail, self.tail.prev)
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.head.next.value

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        return self.tail.prev.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k

# Circular Array

class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = [-1] * k
        self.k = k
        self.p = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.p = (self.p - 1 + self.k) % self.k
        self.arr[self.p] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.arr[(self.p + self.size) % self.k] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.arr[self.p] = -1
        self.p = (self.p + 1) % self.k
        self.size -= 1

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        i = (self.p + self.size - 1) % self.k
        self.arr[i] = -1
        self.size -= 1

        return True

    def getFront(self) -> int:
        return self.arr[self.p]

    def getRear(self) -> int:
        return self.arr[(self.p + self.size - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
