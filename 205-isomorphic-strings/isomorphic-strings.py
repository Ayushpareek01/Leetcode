class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for i in range(min(len(s), len(t))):
            if s[i] in s_dict:
                if s_dict[s[i]] != t[i]:
                    return False
            elif t[i] in t_dict:
                if t_dict[t[i]] != s[i]:
                    return False
            else:
                s_dict[s[i]] = t[i]
                t_dict[t[i]] = s[i]
        return True
        