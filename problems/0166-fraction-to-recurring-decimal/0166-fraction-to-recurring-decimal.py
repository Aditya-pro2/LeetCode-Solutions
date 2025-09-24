class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        f = []
        if (numerator < 0) ^ (denominator < 0):
            f.append("-")
        a, b = abs(numerator), abs(denominator)
        f.append(str(a // b))
        r = a % b
        if r == 0:
            return "".join(f)
        f.append(".")
        m = {}
        while r != 0:
            if r in m:
                f.insert(m[r], "(")
                f.append(")")
                break
            m[r] = len(f)
            r *= 10
            f.append(str(r // b))
            r %= b
        return "".join(f)