class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        if len(s) <= 3:
            return s
        res = list(s)[::-1]
        sol = []
        count = 0
        for i in range(len(res)):
            count += 1
            sol.append(res[i])
            if count == 3 and i != len(res) - 1:
                count = 0
                sol.append(".")
        return "".join(sol[::-1])