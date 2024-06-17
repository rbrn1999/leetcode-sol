# link: https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        arr2_buckets = {num: 0 for num in arr2}
        extras = []
        for num in arr1:
            if num in arr2_buckets:
                arr2_buckets[num] += 1
            else:
                extras.append(num)

        result = []
        for num, count in arr2_buckets.items():
            result.extend([num] * count)

        result.extend(sorted(extras))
        return result

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        max_element = max(arr1)
        count = [0] * (max_element + 1)

        for num in arr1:
            count[num] += 1

        result = []
        for num in arr2:
            result.extend([num] * count[num])
            count[num] = 0

        for num in range(max_element + 1):
            result.extend([num] * count[num])
            count[num] = 0

        return result
