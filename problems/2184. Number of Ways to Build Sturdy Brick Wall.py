# link: https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/

class Solution:
    def buildWall(self, height: int, width: int, bricks: list[int]) -> int:
        row_patterns = []
        join_points = []

        def buildRows(pos: int=0):
            if pos == width:
                row_patterns.append(join_points[:-1])
                return
            if pos > width:
                return

            for brick in bricks:
                join_points.append(pos+brick)
                buildRows(pos+brick)
                join_points.pop()

        buildRows()

        neighbors = [[] for _ in range(len(row_patterns))]

        for i in range(len(row_patterns)):
            if len(row_patterns[i]) == 0:
                neighbors[i].append(i)
            set1 = set(row_patterns[i])
            for j in range(i+1, len(row_patterns)):
                set2 = set(row_patterns[j])
                if len(set1.intersection(set2)) == 0:
                    neighbors[i].append(j)
                    neighbors[j].append(i)


        count = [1] * len(row_patterns)
        for _ in range(height-1):
            new_count = [0] * len(row_patterns)
            for i in range(len(row_patterns)):
                for nei in neighbors[i]:
                    new_count[nei] = (new_count[nei] + count[i]) % (10 ** 9 + 7)

            count = new_count

        return sum(count) % (10 ** 9 + 7)
