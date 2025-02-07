class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = 0
        max_altiude = 0

        for i in gain:
            n += i
            max_altiude = max(max_altiude, n)
        return max_altiude
