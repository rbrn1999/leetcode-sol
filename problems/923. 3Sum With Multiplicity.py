# link: https://leetcode.com/problems/3sum-with-multiplicity/
# Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

# As the answer can be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# Explanation: 
# Enumerating by the values (arr[i], arr[j], arr[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.
# Example 2:

# Input: arr = [1,1,2,2,2,2], target = 5
# Output: 12
# Explanation: 
# arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.

from typing import List
from math import comb
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        total = 0
        d = {}
        for e in arr:
            d.setdefault(e, 0)
            d[e] += 1
        
        arr = list(d.keys())

        for i in range(len(arr)):
            s = set()
            # 3 elements have the same value
            if arr[i]*3 == target:
                total += comb(d[arr[i]],3)

            sum = target - arr[i]
            for j in range(i+1, len(arr)):
                # 2 arr[i]s and 1 arr[j]
                if d[arr[i]] >= 2 and arr[i] + arr[j] == sum:
                    total += comb(d[arr[i]], 2) * d[arr[j]]
                # 1 arr[i] and 2 arr[j]s
                if sum == arr[j]*2:
                    total += d[arr[i]] * comb(d[arr[j]], 2)
                    
                # 3 elements have distinct values
                if (sum - arr[j]) in s:
                    total += d[arr[i]] * d[arr[j]] * d[sum-arr[j]]
                s.add(arr[j])
        return total % int( 10**9 + 7)

arr = [0] * 3000
target = 0

print(Solution().threeSumMulti(arr, target))