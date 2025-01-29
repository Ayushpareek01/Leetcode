class Solution:
    def checkValidString(self, s: str) -> bool:
        star = []
        paren = []
        for i,char in enumerate(s):
            if  char == '(':
                paren.append(i)
            elif char == '*':
                star.append(i)
            else:
                if paren:
                    paren.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while star and paren:
            if paren[-1] > star[-1]:
                return False
            paren.pop()
            star.pop()
        return not paren
        
        
        