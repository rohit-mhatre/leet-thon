class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''.join(filter(str.isalnum, s)).lower()
        left = 0
        right = len(t) - 1
        if t == '':
            return True
        while left < right:
            if t[left] != t[right]:
                return False
            left += 1
            right -= 1
        return True