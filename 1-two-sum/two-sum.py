class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list = {}
        for i in range(len(nums)):
            if target - nums[i] in list:
                return [list[target - nums[i]],i]
            else:
                list[nums[i]]=i
        