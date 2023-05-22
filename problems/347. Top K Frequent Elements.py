# link: https://leetcode.com/problems/top-k-frequent-elements/
# solution reference: https://youtu.be/YPTqKIgVk-k

# Quick Select
# Time Complexity: O(n) (average) O(n^2) (worst)
# Space Complexity: O(n) 
import collections
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        def quickSelect(arr, start, end):
            if start >= end:
                return
            pivot = count[arr[end]]
            left = start
            for i in range(start, end):
                if count[arr[i]] > pivot:
                    arr[left], arr[i] = arr[i], arr[left]
                    left += 1
            
            arr[left], arr[end] = arr[end], arr[left]
            if left > k:
                quickSelect(arr, start, left-1)
            elif left < k:
                quickSelect(arr, left+1, end)

        count = collections.defaultdict(int)
        for num in nums:
            count[num] += 1
        
        nums = list(count.keys())
        quickSelect(nums, 0, len(nums)-1)
        return nums[:k]

# Heap
# Time Complexity: O(nlog(k))
# Space Complexity: O(n) 
# import collections
# import heapq
# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         count = collections.defaultdict(int)
#         for num in nums:
#             count[num] += 1
        
#         heap = [(-freq, num) for num, freq in count.items()]
#         heapq.heapify(heap)
#         answer = []
#         for _ in range(k):
#             answer.append(heapq.heappop(heap)[1])
#         return answer


# Time Complexity: O(kn)
# Space Complexity: O(n)
# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         num_count = defaultdict(lambda: 0)
#         count_nums = [[] for _ in range(len(nums)+1)]
#         for num in nums:
#             num_count[num] = num_count.get(num, 0) + 1
#         for num, count in num_count.items():
#             count_nums[count].append(num)

#         result = []
#         count = len(count_nums)-1
#         while len(result) < k:
#             for num in count_nums[count]:
#                 result.append(num)
#             count -= 1
#         return result


# Time Complexity: O(nlogn)
# Space Complexity: O(n)
#class Solution:
#    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#        d = {}
#        for num in nums:
#            d.setdefault(num, 0)
#            d[num] += 1
#        return sorted(d, key=d.get, reverse=True)[:k]
