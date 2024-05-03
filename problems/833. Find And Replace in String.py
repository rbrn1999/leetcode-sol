# link: https://leetcode.com/problems/find-and-replace-in-string/
#
class Solution:
    def findReplaceString(self, s: str, indices: list[int], sources: list[str], targets: list[str]) -> str:
        result = [c for c in s]
        l = sorted(zip(indices, sources, targets), reverse=True)
        for index, source, target in l:
            if s[index:index+len(source)] == source:
                result[index:index+len(source)] = [c for c in target]

        return ''.join(result)
