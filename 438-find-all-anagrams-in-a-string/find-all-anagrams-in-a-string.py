class Solution:
    def findAnagrams(self, s: str, p: str):
        p_len = len(p)
        s_len = len(s)
        result = []

        if p_len > s_len:
            return result
        p_count = Counter(p)
        s_count = Counter(s[:p_len - 1])
        
        for i in range(p_len - 1, s_len):
            s_count[s[i]] += 1
            if s_count == p_count:
                result.append(i - p_len + 1)
            s_count[s[i - p_len + 1]] -= 1
            if s_count[s[i - p_len + 1]] == 0:
                del s_count[s[i - p_len + 1]]
        
        return result