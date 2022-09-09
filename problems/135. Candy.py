# link: https://leetcode.com/problems/candy/
# solution: https://leetcode.com/problems/candy/discuss/1300194

class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        
        for i in range(n-1):
            if ratings[i+1] > ratings[i]:
                candies[i+1] = candies[i] + 1
                
        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                candies[i-1] = max(candies[i] + 1, candies[i-1])
                
        
        return sum(candies)