class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        f = lambda x : "0" * (4 - len(str(x))) + str(x)
        num1, num2, num3 = f(num1), f(num2), f(num3)
        x = ""
        for i in range(4):
            x += min(num1[i], num2[i], num3[i])
        return int(x)