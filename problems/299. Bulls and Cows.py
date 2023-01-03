# link: https://leetcode.com/problems/bulls-and-cows/

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        sCounter = {}
        gCounter = {}
        n = len(guess)
        for i in range(n):
            if guess[i] == secret[i]:
                bulls += 1
            else:
                sCounter[secret[i]] = sCounter.get(secret[i], 0) + 1
                gCounter[guess[i]] = gCounter.get(guess[i], 0) + 1

        for char in gCounter:
            cows += min(sCounter.get(char, 0), gCounter[char])

        output = str(bulls) + 'A' + str(cows) + 'B'
        return output
