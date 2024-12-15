class Solution:
    def calPoints(self, operations: List[str]) -> int:
        x = []
        for i in operations:
            if i.isnumeric():
                x.append(int(i))
            if i[0] == "-":
                x.append(-int(i[1:]))
            if i == "+":
                x.append(x[-1] + x[-2])
            if i == "D":
                x.append(x[-1] * 2)
            if i == "C":
                x = x[:-1]
        return sum(x)