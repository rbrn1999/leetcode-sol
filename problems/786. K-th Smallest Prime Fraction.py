# link: https://leetcode.com/problems/k-th-smallest-prime-fraction/

# Heap
import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        # (value, [arr[i], arr[j]]), already sorted -> statisfied the heap property
        heap = [(arr[i]/arr[len(arr)-1], i, len(arr)-1) for i in range(len(arr)-1)]

        # remove the smallest value k-1 times
        for _ in range(k-1):
            val, i, j = heapq.heappop(heap)
            if j-1 > i:
                heapq.heappush(heap, (arr[i]/arr[j-1], i, j-1))

        _, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]

# Binary Search
import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        low = 0
        high = 1.0

        # try find a value where exactly values from k-pairs are smaller then this value
        while low < high:
            mid = (low + high) / 2
            max_fraction = 0.0
            total_smaller_fractions = 0
            numerator_idx, denominator_idx = 0, 0
            j = 1

            for i in range(n-1):
                while j < n and arr[i] >= mid * arr[j]: # arr[i] / arr[j] >= mid
                    j += 1

                total_smaller_fractions += (n-j)

                if j == n:
                    break

                if arr[i] / arr[j] > max_fraction:
                    numerator_idx, denominator_idx = i, j
                    max_fraction = arr[i] / arr[j]

            if total_smaller_fractions == k:
                return [arr[numerator_idx], arr[denominator_idx]]
            elif total_smaller_fractions > k:
                high = mid
            else:
                low = mid

        return []
