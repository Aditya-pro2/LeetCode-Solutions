class Solution:
    def decode(self, x: List[int], f: int) -> List[int]:
        a = [f]
        for i in range(len(x)):
            a.append(a[i] ^ x[i])
        return a