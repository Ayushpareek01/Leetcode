class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = Counter(s)
        for i in t:
            count[i] -= 1
            if count[i] < 0:
                return False
        return True
        