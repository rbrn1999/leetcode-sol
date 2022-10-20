# link: https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longestStreak = 0

        s = set(nums)

        while s:
            num = s.pop()

            if num-1 not in s:
                curNum = num
                curStreak = 1

                while curNum+1 in s:
                    curNum += 1
                    curStreak += 1
                    s.remove(curNum)

                longestStreak = max(longestStreak, curStreak)
            else:
                s.add(num)

        return longestStreak

# alternate solution
# reference: https://youtu.be/P6RZZMu_maU

#class Solution:
#    def longestConsecutive(self, nums: List[int]) -> int:
#        longest = 0
#        s = set(nums)
#
#        for num in nums:
#            if (num-1) not in s:
#                length = 1
#                while num+length in s:
#                    length += 1
#                longest = max(length, longest)
#
#        return longest
