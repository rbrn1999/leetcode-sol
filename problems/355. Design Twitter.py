# link: https://leetcode.com/problems/design-twitter/

from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list) # userId: [timestamp, timestamp]
        self.followings = defaultdict(set) # userId: set[userId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        feed = list()
        indexes = {}
        maxHeap = []
        if self.tweets[userId]:
            indexes[userId] = len(self.tweets[userId]) - 1
            t, tweetId = self.tweets[userId][-1]
            maxHeap.append((-t, userId, tweetId))
            indexes[userId] -= 1
        for follow in self.followings[userId]:
            if self.tweets[follow]:
                indexes[follow] = len(self.tweets[follow])-1
                t, tweetId = self.tweets[follow][-1]
                maxHeap.append((-t, follow, tweetId))
                indexes[follow] -= 1
        heapq.heapify(maxHeap)
        while len(feed) < 10 and maxHeap:
            _, follow, tweetId = heapq.heappop(maxHeap)
            feed.append(tweetId)
            if indexes[follow] >= 0:
                t, tweetId = self.tweets[follow][indexes[follow]]
                heapq.heappush(maxHeap, (-t, follow, tweetId))
                indexes[follow] -= 1

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)