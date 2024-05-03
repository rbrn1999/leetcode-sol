from collections import defaultdict
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_char_indices = defaultdict(list)
        for index, char in enumerate(source):
            source_char_indices[char].append(index)

        if any(c not in source_char_indices for c in target):
            return -1

        subsequences = 1
        j = 0
        for target_char in target:
            if source_char_indices[target_char][-1] < j:
                subsequences += 1
                j = source_char_indices[target_char][0]
            else:
                # binary search next indices
                low = 0
                high = len(source_char_indices[target_char])
                while low < high:
                    mid = (low + high) // 2
                    if source_char_indices[target_char][mid] >= j:
                        high = mid
                    else:
                        low += 1

                j = source_char_indices[target_char][low]

            j += 1

        return subsequences

# DP
from collections import defaultdict
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        next_occur = {c: [-1] * len(source) for c in set(source)}
        for i in range(len(source)-1, -1, -1):
            if i < len(source)-1:
                for c in next_occur:
                    next_occur[c][i] = next_occur[c][i+1]

            next_occur[source[i]][i] = i

        if any(c not in next_occur for c in target):
            return -1

        subsequences = 1
        j = 0
        for target_char in target:
            if j > len(source) - 1 or next_occur[target_char][j] == -1:
                subsequences += 1
                j = next_occur[target_char][0]
            else:
                j = next_occur[target_char][j]

            j += 1

        return subsequences
