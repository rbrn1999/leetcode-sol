# link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    # 2022
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []
        
        d = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        result = list(d[digits[0]])
        for i in range(1, len(digits)):
            last = result.copy()
            result = []
            for c in d[digits[i]]:
                result += [l+c for l in last]

        return result


    # 2021
    # def letterCombinations(self, digits: str) -> List[str]:
    #     letters = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
    #     if digits == "":
    #         return []
    #     results = [""]
    #     for digit in digits:
    #         temp = results.copy()
    #         for _ in range(len(letters[digit])-1):
    #             results += temp
    #         for i in range(len(letters[digit])):
    #             for j in range(i*len(temp), (i+1)*len(temp)):
    #                 results[j] += letters[digit][i]
    #     return results
