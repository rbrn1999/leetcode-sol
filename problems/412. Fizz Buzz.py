# link: https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        output = []
        for i in range(1, n+1):
            cur = ""
            if i % 3 == 0:
                cur += "Fizz"
            if i % 5 == 0:
                cur += "Buzz"
            if cur == "":
                cur = str(i)
            output.append(cur)
        return output