class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        m = nums[0]
        for num in range(n):
            if nums[num] > m:
                ans = max(ans, nums[num] - m)
            m = min(m , nums[num])
        return ans
        