# link: https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, num: int) -> str:
        ones = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
        teens = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        order = ["", "Thousand", "Million", "Billion"]

        words = []

        if num == 0:
            return 'Zero'

        exp = -1
        temp = num
        while temp > 0:
            exp += 1
            temp //= 10


        for i in range(exp//3, -1, -1):
            temp = num // 10 ** (i*3)

            if temp // 100 % 10 > 0:
                words.append(ones[temp//100%10 - 1])
                words.append('Hundred')

            if temp % 100 > 0 and temp % 100 < 20:
                if temp % 100 > 10:
                    words.append(teens[temp%100-11])
                else:
                    words.append(ones[temp%100-1])
            else:
                if temp // 10 % 10 > 1:
                    words.append(tens[temp//10%10 - 1])
                if temp % 10 > 0:
                    words.append(ones[temp%10-1])

            if temp % 1000 > 0 and i > 0:
                words.append(order[i])

        return ' '.join(words)
