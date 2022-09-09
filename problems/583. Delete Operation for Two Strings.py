# link: https://leetcode.com/problems/delete-operation-for-two-strings/
# solution: https://www.programiz.com/dsa/longest-common-subsequence
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def lcs_algo(S1, S2):
            m, n = len(S1), len(S2)
            L = [[0 for _ in range(n+1)] for _ in range(m+1)]

            # Building the mtrix in bottom-up way
            for i in range(m+1):
                for j in range(n+1):
                    if i == 0 or j == 0:
                        L[i][j] = 0
                    elif S1[i-1] == S2[j-1]:
                        L[i][j] = L[i-1][j-1] + 1
                    else:
                        L[i][j] = max(L[i-1][j], L[i][j-1])

            return L[m][n]
            ## trace the subsequence
            # index = L[m][n]

            # lcs_algo = [""] * (index+1)
            # lcs_algo[index] = ""

            # i = m
            # j = n
            # while i > 0 and j > 0:

            #     if S1[i-1] == S2[j-1]:
            #         lcs_algo[index-1] = S1[i-1]
            #         i -= 1
            #         j -= 1
            #         index -= 1

            #     elif L[i-1][j] > L[i][j-1]:
            #         i -= 1
            #     else:
            #         j -= 1
        return len(word1) + len(word2) - 2 * lcs_algo(word1, word2)

        # My Brute Force Attempt
        # def match(word1, word2, indice): # word1 contains word2(indice) subsequence
        #     ptr = 0
        #     for i in indice:
        #         if word2[i] not in word1[ptr:]:
        #             return False
        #         else:
        #             ptr = word1[ptr:].index(word2[i]) + ptr + 1
        #             if len(word1)-ptr < (len(indice)-1)-i:
        #             # if ptr > len(word1):
        #                 return False
        #     return True
            
            
        # if len(word1) < len(word2):
        #     word1, word2 = word2, word1
        
        # m, n = len(word1), len(word2)
        
        # for d in range(len(word2)):
        #     for comb in combinations(range(n), n-d):
        #         print(comb)
        #         if match(word1, word2, comb):
        #             return (m-n) + 2*d
        
        # return len(word1) + len(word2)


word1 = "pvhvykrvntdywrhylaprgqmbzqitrhdmxboyw"
word2 = "oelftlrthdmlwznwuritwrvdciho"
print(Solution().minDistance(word1, word2))