# sketch
class Solution:
    def isValid(self, s: str) -> bool:
        string_list = list(s)

        frequency = []

        for c in string_list:
            if c == "(" or c == "[" or c == "{":
                frequency.append(c)
            elif c == ")":
                if not frequency or frequency.pop() != "(":
                    return False
            elif c == "]":
                if not frequency or frequency.pop() != "[":
                    return False
            elif c == "}":
                if not frequency or frequency.pop() != "{":
                    return False
            else:
                frequency.append(c)
        return not frequency


# slightly more optimal:
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in parentheses:
                if not stack or stack.pop() != parentheses[c]:
                    return False
            elif c in parentheses.values():
                stack.append(c)
            else:
                return False

        return not stack


solution = Solution()
s = "([])"
print(solution.isValid(s))
