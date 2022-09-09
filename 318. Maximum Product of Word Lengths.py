# link: https://leetcode.com/problems/maximum-product-of-word-lengths/

from collections import defaultdict
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        len_words = defaultdict(lambda: [])
        for word in words:
            len_words[len(word)].append(word)

        counts = sorted(len_words.keys(), reverse=True)
        pairs = []
        for i in range(len(counts)):
            for j in range(i, len(counts)):
                pairs.append((counts[i], counts[j]))

        pairs.sort(key=lambda x: x[0]*x[1], reverse=True)

        # check from the pairs with the largest product to the smallest
        for l, r in pairs:
            for word1 in len_words[l]:
                for word2 in len_words[r]:
                    if len(set(word1).intersection(word2)) == 0:
                        return len(word1)*len(word2)

        return 0
