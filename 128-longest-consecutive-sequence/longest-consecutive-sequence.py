class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        seq = 0

        for num in numset:
            if (num - 1) not in numset:
                consecutive = 1
                while (num + consecutive) in numset:
                    consecutive = consecutive + 1
                seq = max(seq, consecutive)
        return seq