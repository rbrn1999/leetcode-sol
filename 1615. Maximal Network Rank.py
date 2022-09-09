# link: https://leetcode.com/problems/maximal-network-rank/
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        count_isolate = [[0, set(range(n)) - set([i])] for i in range(n)]
        maxEdgeCount = 0
        secEdgeCount = 0
        for a, b in roads:
            count_isolate[a][0] += 1
            count_isolate[b][0] += 1
            count_isolate[a][1].remove(b)
            count_isolate[b][1].remove(a)

        connectionCount = set([x[0] for x in count_isolate])
        maxEdgeCount = max(connectionCount)
        connectionCount.remove(maxEdgeCount)
        secEdgeCount = max(connectionCount) if len(connectionCount) > 0 else 0


        maxInd = []
        secInd = []
        for i in range(n):
            if count_isolate[i][0] == maxEdgeCount:
                maxInd.append(i)
            elif count_isolate[i][0] == secEdgeCount:
                secInd.append(i)

        for i in range(len(maxInd)):
            for j in range(i+1, len(maxInd)):
                if maxInd[j] in count_isolate[maxInd[i]][1]:
                    return maxEdgeCount * 2

        if len(maxInd) > 1:
            return maxEdgeCount * 2 - 1

        for i in range(len(maxInd)):
            for ind in secInd:
                if ind in count_isolate[maxInd[i]][1]:
                    return maxEdgeCount + secEdgeCount

        return max(maxEdgeCount + secEdgeCount - 1, 1) # prevent edge case: 2, [0, 1]
