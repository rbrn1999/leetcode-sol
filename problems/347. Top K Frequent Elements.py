# link: https://leetcode.com/problems/top-k-frequent-elements/
# solution reference: https://youtu.be/YPTqKIgVk-k

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(lambda: 0)
        count_nums = [[] for _ in range(len(nums)+1)]
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        for num, count in num_count.items():
            count_nums[count].append(num)

        result = []
        count = len(count_nums)-1
        while len(result) < k:
            for num in count_nums[count]:
                result.append(num)
            count -= 1
        return result


# Time Complexity: O(nlogn)
# Space Complexity: O(n)
#class Solution:
#    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#        d = {}
#        for num in nums:
#            d.setdefault(num, 0)
#            d[num] += 1
#        return sorted(d, key=d.get, reverse=True)[:k]
