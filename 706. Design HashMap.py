# link: https://leetcode.com/problems/design-hashmap/

class ListNode:
    def __init__(self, key, val, nextNode=None):
        self.data = (key, val)
        self.nextNode = nextNode
        
class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size

    def calculate_hash_value(self, key):
        return key % self.size
    
    def put(self, key: int, value: int) -> None:
        hv = self.calculate_hash_value(key)
        if self.table[hv] is None:
            self.table[hv] = ListNode(key, value)
            return
        
        node = self.table[hv]
        while node:
            if node.data[0] == key:
                node.data = (key, value)
                return
            if node.nextNode is None:
                node.nextNode = ListNode(key, value)
                return
            else:
                node = node.nextNode

    def get(self, key: int) -> int:
        hv = self.calculate_hash_value(key)
        node = self.table[hv]
        while node:
            if node.data[0] == key:
                return node.data[1]
            else:
                node = node.nextNode
        return -1

    def remove(self, key: int) -> None:
        hv =self.calculate_hash_value(key)
        prev = node = self.table[hv]
        if not node:
            return
        
        if node.data[0] == key:
            self.table[hv] = node.nextNode
        
        node = node.nextNode
        while node:
            if node.data[0] == key:
                prev.nextNode = node.nextNode
                break
            else:
                prev, node = node, node.nextNode
                
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

