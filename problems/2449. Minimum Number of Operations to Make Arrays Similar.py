class Solution:
    def makeSimilar(self, nums: list[int], target: list[int]) -> int:
        countNums = {}
        countTarget = {}
        for num in nums:
            countNums[num] = countNums.get(num, 0) + 1
        for num in target:
            countTarget[num] = countTarget.get(num, 0) + 1
        
        toDelete = []
        for num in countNums:
            if num in countTarget:
                countNums[num], countTarget[num] = countNums[num]-countTarget[num], countTarget[num]-countNums[num]
                if countNums[num] <= 0:
                    toDelete.append(num)
                if countTarget[num] <= 0:
                    del countTarget[num]
        
        for num in toDelete:
            del countNums[num]
        
        oddNums = []
        evenNums = []
        oddTarget = []
        evenTarget = []
        for num in countNums:
            if num % 2:
                oddNums.extend([num]*countNums[num])
            else:
                evenNums.extend([num]*countNums[num])
        for num in countTarget:
            if num % 2:
                oddTarget.extend([num]*countTarget[num])
            else:
                evenTarget.extend([num]*countTarget[num])
        oddNums.sort()
        evenNums.sort()
        oddTarget.sort()
        evenTarget.sort()
        delta = sum(abs((oddNums[i] - oddTarget[i])//2) for i in range(len(oddNums)))
        delta += sum(abs((evenNums[i] - evenTarget[i])//2) for i in range(len(evenNums)))
        return delta // 2