class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        i = 0
        while i < l and n > 0:
            if flowerbed[i] == 0:
                empty_left = (i == 0 or flowerbed[i - 1] == 0)
                empty_right = (i == l - 1 or flowerbed[i + 1] == 0)
                
                if empty_left and empty_right:
                    flowerbed[i] = 1 
                    n -= 1
                    i += 2  
                    continue
            i += 1  

        return n <= 0
