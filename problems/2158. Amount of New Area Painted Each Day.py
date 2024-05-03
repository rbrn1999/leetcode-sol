# link: https://leetcode.com/problems/amount-of-new-area-painted-each-day/

from sortedcontainers import SortedList
class Solution:
    def amountPainted(self, paint: list[list[int]]) -> list[int]:
        n = len(paint)
        records = []
        for i in range(n):
            start, end = paint[i]
            records += [(start, i, True), (end, i, False)]

        records.sort()

        indexes = SortedList()
        answer = [0] * n
        prev_pos = 0

        for pos, index, isStart in records:
            if indexes:
                # extend the interval the comes the earliest and is still not closed
                answer[indexes[0]] += (pos - prev_pos)

            # maintain the ongoing intervals
            if isStart:
                indexes.add(index)
            else:
                indexes.remove(index)

            prev_pos = pos

        return answer
