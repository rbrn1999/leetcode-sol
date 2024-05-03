# link: https://leetcode.com/problems/number-of-matching-subsequences/

# Next Letter Pointers
from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        answer = 0
        word_group = defaultdict(list)
        for word in words:
            it = iter(word)
            word_group[next(it)].append(it) # 'a': 'bc'

        for c in s:
            old_bucket = word_group[c]
            word_group[c] = []

            while old_bucket:
                it = old_bucket.pop()
                next_c = next(it, None)
                if next_c:
                    word_group[next_c].append(it)
                else:
                    answer += 1

        return answer

# Hash Map + Binary Search
from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        char_index = defaultdict(list)
        for i, c in enumerate(s):
            char_index[c].append(i)

        cache = {}
        count = 0
        for word in words:
            if word in cache:
                count += cache[word]
                continue
            prev_i = -1
            isValid = True
            for c in word:
                if c not in char_index:
                    isValid = False
                    break
                # binary search
                low = 0
                high = len(char_index[c])
                while low < high:
                    mid = (low + high) // 2
                    if char_index[c][mid] > prev_i:
                        high = mid
                    else:
                        low += 1

                if low >= len(char_index[c]):
                    isValid = False
                    break
                else:
                    prev_i = char_index[c][low]

            if isValid:
                count += 1
            cache[word] = int(isValid)

        return count
