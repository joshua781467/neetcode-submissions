class Solution:
    def isValid(self, s: str) -> bool:
        m = {')': '(', '}': '{', ']':'['}
        stack = []

        for c in s:
            if c in m:
                if stack and stack[-1] == m.get(c):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

        