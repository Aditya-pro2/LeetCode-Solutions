class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = x = res = 0
        for i in arr:
            s += i
        if s % 3 != 0:
            return False
        else:
            target = s / 3
        for i in arr:
            x += i
            if x == target:
                res += 1
                x = 0
        return res >= 3