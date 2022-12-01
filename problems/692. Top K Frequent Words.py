# link: https://leetcode.com/problems/top-k-frequent-words/

from collections import defaultdict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = defaultdict(lambda: 0)
        for word in words:
            d[word] += 1
        count_word = [(d[word], word) for word in d.keys()]
        count_word.sort(reverse=True)
        start = end = 0
        while start < k:
            if end < len(count_word) and count_word[start][0] == count_word[end][0]:
                end += 1
            else:
                count_word[start:end] = sorted(count_word[start:end], key=lambda x: x[1])
                start = end
        count_word[start:end] = sorted(count_word[start:end], key=lambda x: x[1])
        start = end

        return [word for _, word in count_word[:k]]


'''
heap solution
Time Complexity: O(n*log(n))
Space Complexity: O(n)
'''
import functools
import heapq

@functools.total_ordering
class WordFreq:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        
    # treat less than as greater than to get heapq working as a max-heap
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word <= other.word
        else:
            return self.freq > other.freq
    
    def __eq__(self, other):
        if self.freq == other.freq:
            return self.word == other.word
        else:
            return False

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        result = []
        counter = defaultdict(lambda: 0)
        for word in words:
            counter[word] += 1
            
        wordFreqs = [WordFreq(word, counter[word]) for word in counter]
        heapq.heapify(wordFreqs)
        
        for _ in range(k):
            result.append(heapq.heappop(wordFreqs).word)
        
        return result
