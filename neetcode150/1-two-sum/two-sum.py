class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a dictionary
        map = {}
        for i, n in enumerate(nums):
            temp = target - n
            if temp in map:
                return [map[temp], i]
            map[n] = i
