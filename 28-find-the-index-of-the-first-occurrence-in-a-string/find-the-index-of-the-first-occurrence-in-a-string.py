class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
       # Approach 1
        #n = len(haystack)
        #m = len(needle)
        #for i in range(n - m + 1):
       #     if haystack[i:i+m] == needle:
       #         return i
       # return -1
    
        # apporach 2 
        return haystack.find(needle)

        #apporcah 3
        # n = len(needle)
        # m = len(haystack)
        # for i in range(m):
            # for j in range(n):
                # if needle[i] != haystack[i+j]:
                  # break
            # if j == n:
              #return i
        # return -1