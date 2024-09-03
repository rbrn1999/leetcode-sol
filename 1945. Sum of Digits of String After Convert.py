# link: https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = 0
        for c in s:
            value = ord(c) - ord('a') + 1 
            num += value // 10 + value % 10

        for _ in range(k-1):
            new_num = 0
            while num:
                new_num += num % 10
                num //= 10
            num = new_num
        
        return num