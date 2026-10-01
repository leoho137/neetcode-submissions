class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in "([{":
                stack.append(x)
            elif not stack:
                return False
            elif x == ")":
                if stack.pop() != "(":
                    return False
            elif x == "]":
                if stack.pop() != "[":
                    return False
            elif x == "}":
                if stack.pop() != "{":
                    return False
        if stack:
            return False
        else: 
            return True