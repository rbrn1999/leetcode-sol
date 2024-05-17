# link: https://leetcode.com/problems/design-authentication-manager/
import sys
class Node:
    def __init__(self, tokenId: str, time: int):
        self.tokenId = tokenId
        self.time = time
        self.prev = None
        self.nxt = None

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.token_node = {}
        self.head = Node("", -1)
        self.tail = Node("", sys.maxsize)
        self.head.nxt = self.tail
        self.tail.prev = self.head
        self.size = 0

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.maintain(currentTime)
        node = Node(tokenId, currentTime + self.timeToLive)
        self.insertAtTail(node)

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.maintain(currentTime)
        if tokenId in self.token_node:
            node = self.token_node[tokenId]
            self.remove(node)
            node.time = currentTime + self.timeToLive
            self.insertAtTail(node)


    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.maintain(currentTime)
        cur = self.head.nxt

        while cur and cur != self.tail:
            cur = cur.nxt
        return self.size

    def maintain(self, currentTime: int) -> None:
        cur = self.head.nxt
        while cur and cur.tokenId != "" and cur.time <= currentTime:
            nxt = cur.nxt
            self.remove(cur)
            del self.token_node[cur.tokenId]
            cur = cur.nxt


    def remove(self, node) -> None:
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
        self.size -= 1

    def insertAtTail(self, node) -> None:
        prev = self.tail.prev
        prev.nxt = node
        node.prev = prev
        node.nxt = self.tail
        self.tail.prev = node
        self.token_node[node.tokenId] = node
        self.size += 1

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
