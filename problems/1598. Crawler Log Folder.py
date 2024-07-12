# link: https://leetcode.com/problems/crawler-log-folder/


class Solution:
    def minOperations(self, logs: list[str]) -> int:
        levels = 0
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                levels = max(0, levels-1)
            else:
                levels += 1

        return levels
