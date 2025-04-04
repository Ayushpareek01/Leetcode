class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n = len(word1)
        m = len(word2)

        if n != m:
            return False
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        
        sort1 = sorted(freq1.values())
        sort2 = sorted(freq2.values())

        key = set(freq1.keys()) == set(freq2.keys())

        return sort1 == sort2 and key
        
        