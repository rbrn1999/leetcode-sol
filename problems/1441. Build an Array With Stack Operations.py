# link: https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        stream_num = 1
        ops = []

        for t in target:
            if stream_num < t:
                ops.extend(["Push", "Pop"] * (t-stream_num))
            ops.append("Push")
            stream_num = t+1

        return ops