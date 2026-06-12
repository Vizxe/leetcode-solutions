# https://leetcode.com/problems/partition-array-according-to-given-pivot/
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        same = []
        more = []
        for n in nums:
            if n < pivot:
                less.append(n)
            elif n > pivot: 
                more.append(n)
            else:
                same.append(n)
        return less + same + more
