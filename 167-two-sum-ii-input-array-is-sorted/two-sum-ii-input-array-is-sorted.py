class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointer 0(n)
        left = 0
        right = len(numbers) - 1
        while (left < right):
            temp = numbers[left] + numbers[right]
            if (temp < target):
                left = left + 1
            elif (temp > target):
                right = right - 1
            else:
                return [left + 1, right + 1]