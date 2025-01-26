class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        close = 0
        for char in s:
            if char == '(':
                open += 1
            elif char == ')':
                if open > 0:
                    open -=1
                else:
                    close +=1
        return open + close
        