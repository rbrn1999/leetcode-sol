# link: https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {order[i]: i for i in range(26)}

        def compare(s1: str, s2: str) -> int:
            n = min(len(s1), len(s2))
            for i in range(n):
                if order_dict[s1[i]] < order_dict[s2[i]]:
                    return -1
                elif order_dict[s1[i]] > order_dict[s2[i]]:
                    return 1

            if len(s1) < len(s2):
                return -1
            elif len(s1) > len(s2):
                return 1
            else:
                return 0

        for i in range(len(words)-1):
            if compare(words[i], words[i+1]) == 1:
                return False

        return True

# with sort function
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {order[i]: i for i in range(26)}

        def compare(s1: str, s2: str) -> int:
            n = min(len(s1), len(s2))
            for i in range(n):
                if order_dict[s1[i]] < order_dict[s2[i]]:
                    return -1
                elif order_dict[s1[i]] > order_dict[s2[i]]:
                    return 1

            if len(s1) < len(s2):
                return -1
            elif len(s1) > len(s2):
                return 1
            else:
                return 0

        for i in range(len(words)-1):
            if compare(words[i], words[i+1]) == 1:
                return False

        return True

