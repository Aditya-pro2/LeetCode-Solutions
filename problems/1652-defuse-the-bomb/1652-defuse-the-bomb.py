class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        if k == 0:
            return ans
        s = 1 if k > 0 else n + k
        e = k if k > 0 else n - 1
        x = sum(code[i % n] for i in range(s, e + 1))
        for i in range(n):
            ans[i] = x
            x -= code[(s + i) % n]
            x += code[(e + i + 1) % n]
        return ans