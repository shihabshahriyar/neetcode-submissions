class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i, height1 in enumerate(heights):
            for j, height2 in enumerate(heights):
                if i != j:
                    length = abs(i - j)
                    height = min(height1, height2)
                    maxArea = max(maxArea, length * height)
        return maxArea