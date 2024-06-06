# link: https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        n = len(arr)
        prefixXor = [0] # prefixXor[i] = prefix xor from arr[0] to arr[i-1]
        result = 0
        for num in arr:
            prefixXor.append(num ^ prefixXor[-1])

        for i in range(n-1):
            for k in range(i+1, n):
                # arr[i] ^ arr[i + 1] ^ ... ^ arr[k - 1] ^ arr[k] = 0
                # for any j from (i, k]: a ^ b = 0
                # a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
                # b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
                if prefixXor[i] ^ prefixXor[k+1] == 0:
                    result += k - i

        return result


# Optimal
from collections import defaultdict
class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        n = len(arr)
        result = 0
        XOR_value_counts = defaultdict(int) # count: appearances of prefix xor == count
        XOR_value_index_sums = defaultdict(int) # key: sum of indices where [prefix xor [0, i)] == key

        XOR_value_counts[0] = 1
        XOR_value_index_sums[0] = 0

        prefix_xor = 0
        for k, num in enumerate(arr):
            xor = num ^ prefix_xor
            # (k - i), (k - i'), (k - i'') -> n*k - sum(all i)
            result += XOR_value_counts[xor] * k - XOR_value_index_sums[xor]

            prefix_xor = xor
            XOR_value_counts[prefix_xor] += 1
            XOR_value_index_sums[prefix_xor] += k + 1

        return result
