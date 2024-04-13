class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch == '+':
                stack.append(stack.pop() + stack.pop())
            elif ch == '-':
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append(temp2-temp1)
            elif ch == '*':
                stack.append(stack.pop() * stack.pop())
            elif ch == '/':
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append(int(float(temp2/temp1)))
            else:
                stack.append(int(ch))
        return stack[0]