class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Map = {"(":")","{":"}","[":"]"}
        for ch in s:
            if ch in Map:
                stack.append(ch)
            elif len(stack) == 0 or Map[stack.pop()] != ch:
                return False
        return len(stack) == 0

