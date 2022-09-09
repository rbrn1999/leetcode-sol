# link: https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

from collections import defaultdict
from string import ascii_lowercase

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:

        convertedWordSets = defaultdict(set)
        # {wordLength: charSet}
        targetWordSets = defaultdict(lambda: 0)
        # {charSet: countOfAppearances}

        for word in startWords:
            for c in ascii_lowercase:
                if c in word:
                    continue
                convertedWordSets[len(word)+1].add(frozenset(word+c))

        for word in targetWords:
            targetWordSets[frozenset(word)] += 1

        return sum(targetWordSets[t] for t in targetWordSets if t in convertedWordSets[len(t)])
