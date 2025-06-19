class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_start = 0
        min_length = math.inf
        window_sum = 0

        for window_end in range(0, len(nums)):
            window_sum += nums[window_end]


            while window_sum>=target:
                min_length = min(min_length, window_end-window_start+1)
                window_sum -= nums[window_start]
                window_start += 1

        if min_length == math.inf:
                return 0
        return min_length