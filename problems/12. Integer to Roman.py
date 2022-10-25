# link: https://leetcode.com/problems/integer-to-roman/

from collections import deque
class Solution:
    def intToRoman(self, num: int) -> str:
        rom = deque([['I', 'V'], ['X', 'L'], ['C', 'D'], ['M']])

        result = deque()
        while num > 0 and len(rom)>1:
            cur = rom.popleft()
            if num % 10 == 4:
                result.appendleft(cur[0]+cur[1])
            elif num % 10 == 9:
                result.appendleft(cur[0]+rom[0][0])
            else:
                result.appendleft(cur[1]*(num%10>=5) + cur[0]*(num%5))
            num //= 10

        result.appendleft(rom.popleft()[0]*num)
        return ''.join(result)

# solution 2021 April
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         value = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
#         roman = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}

#         result = ""

#         if num % 10 == 9:
#             result = "IX" + result
#         elif num % 5 == 4:
#             result = "IV" + result
#         else:
#             result = 'I' * (num%5) + result

#         if 9 > num % 10 >= 5:
#             result = 'V' + result

#         if num//10 % 10 == 9:
#             result = "XC" + result
#         elif num//10 % 5 == 4:
#             result = "XL" + result
#         else:
#             result = 'X' * (num//10%5) + result

#         if 9 > num//10 % 10 >= 5:
#             result = 'L' + result

#         if num//100 % 10 == 9:
#             result = "CM" + result
#         elif num//100 % 5 == 4:
#             result = "CD" + result
#         else:
#             result = 'C' * (num//100%5) + result

#         if 9 > num//100 % 10 >= 5:
#             result = 'D' + result

#         result = 'M' * (num // 1000) + result

#         return result
