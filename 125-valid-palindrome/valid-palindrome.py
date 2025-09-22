class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''
        for a in s:
            if a.isalnum():
                temp += a.lower()
        return (temp == temp[::-1])