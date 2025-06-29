class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        small_diff = math.inf

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                target_diff = target - currSum
                if target_diff == 0:
                    return currSum

                if abs(small_diff) >= abs(target_diff):
                    small_diff = target_diff

                if target_diff > 0:
                    left += 1
                else:
                    right -= 1

        return target - small_diff
            

