class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n= len(s)
        for i in range(1, n//2 + 1):
            if n%1 == 0:
                s2 = s[:i]
                s3 = s2 *(n//i)
                if s3 == s:
                    return True
        return False

                

        