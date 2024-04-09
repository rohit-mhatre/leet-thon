class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        while (left < right):
            maxArea = max(maxArea, min(height[left],height[right])*(right-left))
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return maxArea
