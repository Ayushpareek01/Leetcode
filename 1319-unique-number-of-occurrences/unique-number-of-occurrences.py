class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_map = {}
        for num in arr:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1

        occurrences = list(count_map.values())
        n = len(occurrences)
    
        for i in range(n):
            for j in range(i + 1, n):
                if occurrences[i] == occurrences[j]:
                    return False  
                
        return True 

        