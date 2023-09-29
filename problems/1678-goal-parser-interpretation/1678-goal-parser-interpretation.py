class Solution:
    def interpret(self, c: str) -> str:
        c = c.replace("()", "o")
        return c.replace("(al)", "al")