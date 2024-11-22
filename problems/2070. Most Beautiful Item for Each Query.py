# link: https://leetcode.com/problems/most-beautiful-item-for-each-query/

class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        items.sort(key=lambda x: (x[0], -x[1]))
        price_max_beauty = [[0, 0]]
        for i in range(len(items)):
            if items[i][0] == price_max_beauty[-1][0]:
                continue
            price_max_beauty.append([items[i][0], max(items[i][1], price_max_beauty[-1][1])])

        result = []
        for q in queries:
            low = 0
            high = len(price_max_beauty)
            while low < high:
                mid = (low + high) // 2
                if price_max_beauty[mid][0] <= q:
                    low = mid + 1
                else:
                    high = mid
            i = low
            result.append(price_max_beauty[i-1][1])

        return result
