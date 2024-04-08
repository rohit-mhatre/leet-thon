class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(nums):
            temp = target - n
            if temp in map:
                return [map[temp], i]
            map[n] = i