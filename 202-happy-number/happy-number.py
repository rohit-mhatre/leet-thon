class Solution:
    def isHappy(self, n: int) -> bool:
        def get_squared_sum(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num = num//10
            return total

        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = get_squared_sum(n)


        return n == 1
