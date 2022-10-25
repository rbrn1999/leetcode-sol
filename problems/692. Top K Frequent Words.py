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

        return [word for count, word in count_word[:k]]
