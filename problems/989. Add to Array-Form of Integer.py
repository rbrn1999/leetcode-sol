# link: https://leetcode.com/problems/add-to-array-form-of-integer/

# solution reference: https://leetcode.com/problems/add-to-array-form-of-integer/solutions/234488/java-c-python-take-k-itself-as-a-carry/
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num)-1, -1, -1):
            num[i] += k
            k = num[i] // 10
            num[i] %= 10
        return ([int(c) for c in str(k)] if k > 0 else []) + num
