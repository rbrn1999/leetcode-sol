# link: https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        arr = []
        accumulate = 0 # arr[0] xor arr[1] xor ... arr[i], arr[i] = pref[i] xor arr[0~i-1]
        for p in pref:
            val = p ^ accumulate
            arr.append(val)
            accumulate ^= val
        return arr
    
class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        # pref[i] ^ pref[i+1] = arr[i+1] (The arr[0~i] xor(s) cancelled out)
        return [pref[0]] + [pref[i] ^ pref[i-1] for i in range(1, len(pref))]