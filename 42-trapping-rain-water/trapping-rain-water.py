class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0 
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        maxHeight = 0

        while left<right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                maxHeight += (left_max - height[left])

            else:
                right -= 1
                right_max = max(right_max, height[right])
                maxHeight += (right_max - height[right])

        return maxHeight