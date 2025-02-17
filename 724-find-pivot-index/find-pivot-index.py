class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        r = sum(nums)

        for idx , num in enumerate(nums):
            r -= num
            if l == r:
                return idx
            l += num
        return -1
