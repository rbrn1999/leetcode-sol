# link: https://leetcode.com/problems/sequence-reconstruction/

from collections import deque, defaultdict
class Solution:
    def sequenceReconstruction(self, nums: list[int], sequences: list[List[int]]) -> bool:
        n = len(nums)
        indegree = [0] * n # indegree[i]: indegree of i+1
        adj = defaultdict(set)
        for seq in sequences:
            for i in range(len(seq)-1):
                if seq[i+1] in adj[seq[i]]:
                    continue
                adj[seq[i]].add(seq[i+1])
                indegree[seq[i+1]-1] += 1
        
        order = []
        q = deque()
        q.extend([(i+1) for i in range(n) if indegree[i] == 0])
        if len(q) > 1:
            return False

        while q:
            num = q.popleft()
            order.append(num)
            for next_num in adj[num]:
                indegree[next_num-1] -= 1
                if indegree[next_num-1] == 0:
                    if len(q) > 0:
                        return False
                    q.append(next_num)
        
        return order == nums