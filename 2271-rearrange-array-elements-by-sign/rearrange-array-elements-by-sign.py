class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        for num in nums:
            if num < 0:
                arr1.append(num)
            else:
                arr2.append(num)
        idx1 = 0
        idx2 = 0
        i = 0
        while idx1 < len(arr1) and idx2 < len(arr2):
            if i % 2 == 0:
                nums[i] = arr2[idx2]
                idx2 += 1
            else:
                nums[i] = arr1[idx1]
                idx1 += 1
            i += 1
        while idx1 < len(arr1):
            nums[i] = arr1[idx1]
            idx1 += 1
            i += 1
        while idx2 < len(arr2):
            nums[i] = arr2[idx2]
            idx2 += 1
            i += 1
        return nums