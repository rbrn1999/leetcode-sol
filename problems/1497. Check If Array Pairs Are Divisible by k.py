# link: https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

# Array

class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        mod_count = [0] * k # mod_count[i] -> count of num % k == i+1
        for num in arr:
            mod_count[(num+k)%k] += 1

        l = 1
        r = k-1
        while l <= r:
            if mod_count[l] != mod_count[r]:
                return False
            l += 1
            r -= 1

        return mod_count[0] % 2 == 0

# Hash Table

class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        mod_count = {}
        for num in arr:
            mod_count[(num+k)%k] = mod_count.get((num+k)%k, 0) + 1

        if mod_count.get(0, 0) % 2 == 1:
            return False

        for num in arr:
            r = num % k
            if r > 0 and mod_count.get(r, 0) != mod_count.get(k-r, 0):
                return False

        return True
