class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closestSum = math.inf
        nums.sort()

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
             
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
                target_diff = target - currSum

                if target_diff == 0:
                    return currSum
                if abs(closestSum) >= abs(target_diff):
                    closestSum = target_diff
                
                if target_diff < 0:
                    r -= 1
                else: 
                    l += 1
        return target - closestSum
