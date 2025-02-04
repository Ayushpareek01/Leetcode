class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x: float, n: int) -> float:
            if n == 0:
                return 1 
            
            half = power(x, n // 2)
            result = half * half
            return result if n % 2 == 0 else result * x
        return power(x, n) if n >= 0 else 1 / power(x, -n)
        