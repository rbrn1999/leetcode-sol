# link: https://leetcode.com/problems/find-the-closest-palindrome/

class Solution:
    def nearestPalindromic(self, n: str) -> str:

        # check edge cases: '11', '101', '1001' ...
        if len(n) >= 2 and n[0] == '1' and int(n[-1]) <= 1 and all(c == '0' for c in n[1:-1]):
            return '9' * (len(n)-1)
        # check edge cases: '99', '999', '9999' ...
        if len(n) >= 2 and all(c == '9' for c in n):
            return '1' + '0' * (len(n) - 1) + '1'


        mid = len(n) // 2
        if len(n) % 2 == 0:
            mid -= 1
        result = "0"
        diff = float('inf')

        front = int(n[:mid+1])

        # [front - 1] + [front - 1].reversed()
        front -= 1
        candidate = str(front) + str(front)[:len(str(front)) - (len(n)%2)][::-1]
        if abs(int(candidate) - int(n)) < diff:
            result = candidate
            diff = abs(int(candidate) - int(n))
        
        front += 1

        # front + front.reversed()
        candidate = n[:mid+1] + n[:mid+1-(len(n)%2)][::-1]
        if candidate != n and abs(int(candidate) - int(n)) < diff:
            result = candidate
            diff = abs(int(candidate) - int(n))
        

        # [front + 1] + [front + 1].reversed()
        front += 1
        candidate = str(front) + str(front)[:len(str(front)) - (len(n)%2)][::-1]
        if abs(int(candidate) - int(n)) < diff:
            result = candidate
            diff = abs(int(candidate) - int(n))

        
        return result