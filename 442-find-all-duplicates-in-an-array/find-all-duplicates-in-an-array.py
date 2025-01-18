class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        duplicate = []
        for num in range(1, n):
            if nums[num] == nums[num -1]:
                duplicate.append(nums[num])
        return duplicate

        