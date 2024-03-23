class Solution:
    def sumOfEncryptedInt(self, a: List[int]) -> int:
        for i in range(len(a)):
            x = list(str(a[i]))
            a[i] = int(max(x) * len(x))
        return sum(a)