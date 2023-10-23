# link: https://leetcode.com/problems/last-visited-integers/

class Solution:
    def lastVisitedIntegers(self, words: list[str]) -> list[int]:
        words.append("0")
        nums = []
        ans = []
        count = 0
        for word in words:
            if word == "prev":
                count += 1
            else:
                nums.append(int(word))
                count = 0
            if count > 0:
                ans.append(nums[-count] if count <= len(nums) else -1)
        
        return ans