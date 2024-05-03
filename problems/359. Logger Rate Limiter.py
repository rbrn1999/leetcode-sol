# link: https://leetcode.com/problems/logger-rate-limiter/

# Hash Table
class Logger:

    def __init__(self):
        self.message_time = {}
        self.dq = deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if self.message_time.get(message, -10) + 10 > timestamp:
            return False
        else:
            self.message_time[message] = timestamp
            return True


# Queue
from collections import deque
class Logger:

    def __init__(self):
        self.message_time = {}
        self.dq = deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if self.message_time.get(message, -10) + 10 > timestamp:
            return False
        else:
            while self.dq and self.dq[0][1] + 10 < timestamp:
                old_message, _ = self.dq.popleft()
                del self.message_time[old_message]
            self.message_time[message] = timestamp
            self.dq.append((message, timestamp))
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)