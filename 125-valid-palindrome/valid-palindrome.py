class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''
        for ch in s:
            if ch.isalpha() or ch.isdigit():
                temp = temp + ch.lower()
        return (temp == temp[::-1])