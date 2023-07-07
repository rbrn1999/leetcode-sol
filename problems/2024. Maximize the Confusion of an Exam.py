# link: https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        answer = 1
        left = 0
        kT = k
        for right in range(len(answerKey)):
            if answerKey[right] == 'F':
                if kT > 0:
                    kT -= 1
                else:
                    while answerKey[left] != 'F':
                        left += 1
                    left += 1
                    left = min(left, right)
            answer = max(answer, right-left+1)

        left = 0
        kF = k
        for right in range(len(answerKey)):
            if answerKey[right] == 'T':
                if kF > 0:
                    kF -= 1
                else:
                    while answerKey[left] != 'T':
                        left += 1
                    left += 1
                    left = min(left, right)
            answer = max(answer, right-left+1)

        return answer

