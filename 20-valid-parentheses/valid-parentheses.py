class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Map = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch not in Map:
                stack.append(ch)
                continue
            if not stack or stack[-1] != Map[ch]:
                return False
            stack.pop()

        return not stack