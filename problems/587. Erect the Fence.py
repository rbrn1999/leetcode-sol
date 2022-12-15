# link: https://leetcode.com/problems/erect-the-fence/
# solution reference: https://leetcode.com/problems/erect-the-fence/solutions/1442266/a-detailed-explanation-with-diagrams-graham-scan/comments/1082215/

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cmp(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3

            # (y3-y2)/(x3-x2) - (y2-y1)/(x2-x1)
            return (y3 - y2) * (x2 - x1) - (y2 - y1) * (x3 - x2)

        points = sorted(trees)

        lowerHalf = []
        upperHalf = []

        for point in points:
            while len(lowerHalf) >= 2 and cmp(lowerHalf[-2], lowerHalf[-1], point) < 0:
                lowerHalf.pop()
            while len(upperHalf) >= 2 and cmp(upperHalf[-2], upperHalf[-1], point) > 0:
                upperHalf.pop()

            lowerHalf.append(tuple(point))
            upperHalf.append(tuple(point))

        return list(set(lowerHalf + upperHalf))
