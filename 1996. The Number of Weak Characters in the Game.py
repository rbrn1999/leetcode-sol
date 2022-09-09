# link: https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
# solution ref: https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/discuss/1445198

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        result = 0
        properties.sort(key=lambda x: (-x[0], x[1]))
        # attack: largest -> lowest (descending)
        # tie breaker: defense assending

        max_d = 0

        for _, d in properties:
            # the current a is strickly lesser then the max_d's original a(orig_a): go to d<max_d
            # otherwise(cur_a==orig_a), d will be equal or greater then max_d: go to else statement
            if d < max_d:
                result += 1
            else:
                max_d = d

        return result

        # the idea:
        # compare attack by sorting
        # compare defense by keeping track of the largest possible previous defense

        # edge case cur_attack==prev_attack and cur_defense>prev_defence:
        # sol: sort tie attacks in assending defense order to avoid these cases
