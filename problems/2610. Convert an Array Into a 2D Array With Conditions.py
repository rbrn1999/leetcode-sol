# link: https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        result = []

        while freq:
            result.append(list(freq.keys()))
            for num in result[-1]:
                freq[num] -= 1
                if freq[num] == 0:
                    del freq[num]
        
        return result