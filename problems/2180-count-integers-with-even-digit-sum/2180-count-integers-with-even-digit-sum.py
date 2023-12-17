class Solution:
    def countEven(self, num: int) -> int:
        n = sum(list(map(int, str(num).strip())))
        return num // 2 if n % 2 == 0 else ceil(num / 2) - 1