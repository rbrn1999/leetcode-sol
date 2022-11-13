# link: https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        self.length = k
        self.arr = [-1] * k
        self.head = -1
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.head = self.tail = 0
            self.arr[0] = value
            return True
        else:
            self.tail = (self.tail + 1) % self.length
            self.arr[self.tail] = value
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        elif self.head == self.tail:
            self.head = self.tail = -1
            return True
        else:
            self.head = (self.head + 1) % self.length
            return True
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.arr[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.arr[self.tail]

    def isEmpty(self) -> bool:
        return self.head == -1

    def isFull(self) -> bool:
        return (self.tail + 1) % self.length == self.head


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
