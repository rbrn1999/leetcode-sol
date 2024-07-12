# link: https://leetcode.com/problems/water-bottles/

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalBottles = numBottles
        while numBottles >= numExchange: # numBottles are empty bottles
            totalBottles += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange
        return totalBottles