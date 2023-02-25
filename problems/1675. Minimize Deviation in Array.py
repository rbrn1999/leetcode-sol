import heapq
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        nums = list(set(nums))
        max_nums = [num * 2 if num % 2 == 1 else num for num in nums]
        for i in range(len(nums)):
            while nums[i] % 2 == 0:
                nums[i] //= 2

        minHeap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(minHeap)
        maxNum = max(nums)
        deviation = float('inf')
        while True:
            minNum, minInd = minHeap[0]
            deviation = min(deviation, maxNum - minNum)

            if minNum * 2 <= max_nums[minInd]:
                newNum = minNum * 2
                heapq.heapreplace(minHeap, (newNum, minInd))
                nums[minInd] = newNum
                maxNum = max(maxNum, newNum)
            else:
                break

        return deviation