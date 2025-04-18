class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(array):
            if len(array) <= 1:
                return array
            
            mid = len(array) // 2
            left_half = merge_sort(array[:mid])
            right_half = merge_sort(array[mid:])
            
            return merge(left_half, right_half)
        
        def merge(left, right):
            sorted_array = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sorted_array.append(left[i])
                    i += 1
                else:
                    sorted_array.append(right[j])
                    j += 1
            
            while i < len(left):
                sorted_array.append(left[i])
                i += 1
            
            while j < len(right):
                sorted_array.append(right[j])
                j += 1
            
            return sorted_array
        
        
        return merge_sort(nums)