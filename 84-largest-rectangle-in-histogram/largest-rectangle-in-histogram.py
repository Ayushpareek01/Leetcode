class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        left = [0] * n
        right = [0] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = 0 if not stack else stack[-1] + 1
            stack.append(i)
        
        stack.clear()

        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = n - 1 if not stack else stack[-1] - 1
            stack.append(i)

        
        max_area = 0
        for i in range(n):
            width = right[i] - left[i] + 1
            max_area = max(max_area, heights[i] * width)

        return max_area
