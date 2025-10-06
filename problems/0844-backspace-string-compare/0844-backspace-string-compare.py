class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def fun(x):
            p = ""
            for i in x:
                if i == '#':
                    p = p[:-1]
                else:
                    p += i
            return p
        return fun(s) == fun(t)