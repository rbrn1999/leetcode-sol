# link: https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    @staticmethod
    def convertNumber(mapping: list[int], num: int) -> int:
        if num == 0:
            return mapping[0]

        converted_num = 0
        e = 0
        while num > 0:
            converted_num += mapping[num%10] * (10 ** e)
            e += 1
            num //= 10

        return converted_num

    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        sorted_index = sorted(list(range(len(nums))), key=lambda i: (self.__class__.convertNumber(mapping, nums[i]), i))
        return [nums[i] for i in sorted_index]
