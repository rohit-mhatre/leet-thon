class Solution:
    def isHappy(self, n: int) -> bool:
        fast, slow = n, n
        def get_squared_sum(n):
            total = 0
            while (n>0):
                digit = n % 10
                total += digit * digit
                n //= 10
            return total
        
        while True:
            slow = get_squared_sum(slow)
            fast = get_squared_sum(get_squared_sum(fast))

            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False