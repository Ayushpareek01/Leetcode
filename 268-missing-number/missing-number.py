class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        totalsum = sum(nums)
        esum = (n*(n+1))//2

        return esum - totalsum
        