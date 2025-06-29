class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        left, right = 0, len(nums) - 1
        highidx = len(nums) - 1
        while left <= right:
            leftsquared = nums[left] * nums[left]
            rightsquared = nums[right] * nums[right]

            if leftsquared > rightsquared:
                result[highidx] = leftsquared
                left += 1
            else:
                result[highidx] = rightsquared
                right -= 1
            highidx -= 1
        
        return result