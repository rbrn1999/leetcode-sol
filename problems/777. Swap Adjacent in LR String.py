# link: https://leetcode.com/problems/swap-adjacent-in-lr-string/

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start_r = []
        start_l = []
        end_r = []
        end_l = []
        start_pattern = []
        end_pattern = []
        for i in range(len(start)):
            if start[i] == 'R':
                start_r.append(i)
                start_pattern.append('R')
            elif start[i] == 'L':
                start_l.append(i)
                start_pattern.append('L')

            if end[i] == 'R':
                end_r.append(i)
                end_pattern.append('R')
            elif end[i] == 'L':
                end_l.append(i)
                end_pattern.append('L')


        # check order of Ls and Rs
        if start_pattern != end_pattern:
            return False

        # L and R doesn't need to cross at this point
        # each R in start should be at the position or on the left of the coresponding R in end
        # And viseversa for L
        for start_i, end_i in zip(start_r, end_r):
            if start_i > end_i:
                return False

        for start_i, end_i in zip(start_l, end_l):
            if start_i < end_i:
                return False

        return True
