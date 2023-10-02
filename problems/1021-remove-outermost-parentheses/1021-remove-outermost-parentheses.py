class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        r, x = [], 0
        for c in s:
            if (c == '(' and x > 0) or (c == ')' and x > 1):
                r.append(c)
            x += 1 if c == '(' else -1
        return "".join(r)