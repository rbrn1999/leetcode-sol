# link: https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        for i in range(len(arr)-1):
            arr[i+1] ^= arr[i]
        return [ arr[r]^arr[l-1] if l > 0 else arr[r] for l, r in queries]
    # brute force
    # def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
    #     result = []
    #     for start, end in queries:
    #         val = 0
    #         for i in range(start, end+1):
    #             val ^= arr[i]
    #         result.append(val)
    #     return result
    