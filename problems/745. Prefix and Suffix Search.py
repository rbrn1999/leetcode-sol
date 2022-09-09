# link: https://leetcode.com/problems/prefix-and-suffix-search/
# solution: https://leetcode.com/problems/prefix-and-suffix-search/discuss/1185171

from itertools import product

class WordFilter:
    def __init__(self, words: list[str]):
        from collections import defaultdict
        self.d = defaultdict(lambda: -1)
        for i, word in enumerate(words):
            for p, s in product(range(len(word)+1), repeat=2):
                self.d[word[:p+1], word[s:]] = i
    
        
    def f(self, prefix: str, suffix: str) -> int:
        return self.d[prefix, suffix]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)