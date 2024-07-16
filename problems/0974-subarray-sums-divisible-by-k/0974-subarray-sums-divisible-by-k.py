class Solution:
    def subarraysDivByK(self, a: List[int], k: int) -> int:
        s = [0] * k
        s[0] += 1
        c = cs = 0
        for i in range(len(a)):
            cs = (cs + a[i] % k + k) % k
            c += s[cs]
            s[cs] += 1
        return c