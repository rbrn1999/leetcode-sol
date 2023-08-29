# link: https://leetcode.com/problems/minimum-penalty-for-a-shop/

# 2-pass straight forward
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        Y_right = customers.count('Y')
        N_left = 0
        min_penalty = Y_right
        answer = 0
        for i in range(1, n+1):
            N_left += int(customers[i-1] == 'N')
            Y_right -= int(customers[i-1] == 'Y')
            penalty = N_left + Y_right
            if penalty < min_penalty:
                min_penalty = penalty
                answer = i
        
        return answer
    
# alternative solution
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
	    # default: closed at hour 0
        answer = 0
        min_penalty = penalty = customers.count('Y')
        for i in range(n):
			# closed at i+1: add customer[i] to the "left"
            if customers[i] == 'Y':
                penalty -= 1
            else:
                penalty += 1
            if penalty < min_penalty:
                min_penalty = penalty
                answer = i+1
        
        return answer

# one pass: only care relative value

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        penalty = min_penalty = 0
        answer = 0
        for i in range(n):
            if customers[i] == 'Y':
                penalty -= 1
            else:
                penalty += 1
            if penalty < min_penalty:
                min_penalty = penalty
                answer = i+1
        
        return answer


