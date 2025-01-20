class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()

        reverseword = word[::-1]

        return ' '.join(reverseword)
        