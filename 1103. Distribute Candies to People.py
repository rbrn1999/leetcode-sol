# link: https://leetcode.com/problems/distribute-candies-to-people/

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0]*num_people
        cur = 0
        while candies > 0:
            if candies <= cur+1:
                result[cur % num_people] += candies
                return result
            else:
                result[cur % num_people] += cur+1
                candies -= cur+1
                cur += 1

        return result
