class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_length = 0
        window_start = 0
        fruits_freq = {}

        for window_end in range(len(fruits)):
            right_fruit = fruits[window_end]

            if right_fruit not in fruits_freq:
                fruits_freq[right_fruit] = 0
            fruits_freq[right_fruit] += 1

            while len(fruits_freq) > 2:
                left_fruit = fruits[window_start]
                fruits_freq[left_fruit] -= 1
                if fruits_freq[left_fruit] == 0:
                    del fruits_freq[left_fruit]
                window_start += 1
            max_length = max(max_length, window_end-window_start+1)

        return max_length
            