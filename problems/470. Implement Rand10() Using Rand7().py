# link: https://leetcode.com/problems/implement-rand10-using-rand7/

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

# Approach 1
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        # will get 1~49
        val = (rand7()-1) * 7 + rand7()

        # reject 41~49 and resample
        while val > 40:
            val = (rand7()-1) * 7 + rand7()

        return val % 10 + 1

# Approach 2
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """

        while True:
            # get 1~49
            val = (rand7()-1) * 7 + rand7()
            # reject 41~49
            if val <= 40:
                return val % 10 + 1

            # get 1~63
            val = (val - 40 - 1) * 7 + rand7()
            # reject 61~63
            if val <= 60:
                return val % 10 + 1

            # get 1~21
            val = (val - 60 - 1) * 7 + rand7()
            # reject 21
            if val <= 20:
                return val % 10 + 1


        return -1
