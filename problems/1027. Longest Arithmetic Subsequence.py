# link: https://leetcode.com/problems/longest-arithmetic-subsequence/

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        d = {} # {last element: {diff: max length}}
        result = 0
        for num in nums:
            # calculate sequence that ends at num
            temp = {}
            for key in d.keys():
                diff = num - key
                temp[diff] = max(d[key][diff] + 1 if diff in d[key] else 2, temp.get(diff, 0))
                # update longest sequence
                result = max(result, temp[diff])

            # update dictionary
            if num not in d:
                d[num] = temp
            else:
                for diff in temp:
                    d[num][diff] = max(d[num].get(diff, 0), temp[diff])

        return result

