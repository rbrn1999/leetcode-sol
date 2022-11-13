# link: https://leetcode.com/problems/convert-the-temperature/

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        res = []
        res.append(celsius + 273.15)
        res.append(celsius * 1.8 + 32)
        return res
