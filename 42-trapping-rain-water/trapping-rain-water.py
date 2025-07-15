class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        water = 0
        left_max = right_max = -1
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1
        return water

