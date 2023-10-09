# link: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        answer = 0
        for num in range(n+1):
            if num % m > 0:
                answer += num
            else:
                answer -= num
        
        return answer
        