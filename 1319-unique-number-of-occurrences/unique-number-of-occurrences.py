class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map1 = Counter(arr)
        count = list(map1.values())
        return len(count) == len(set(count))


        