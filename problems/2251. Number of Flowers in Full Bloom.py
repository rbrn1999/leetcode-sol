# link: https://leetcode.com/problems/number-of-flowers-in-full-bloom/

class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        bloom = []
        for start, end in flowers:
            bloom.append((start, 1))
            bloom.append((end+1, -1))
        
        bloom.sort(reverse=True)
        people = sorted([(p, i) for (i, p) in enumerate(people)])
        answer = [0] * len(people)
        count = 0
        for p, i in people:
            while bloom and bloom[-1][0] <= p:
                count += bloom.pop()[1]
            answer[i] = count
        
        return answer