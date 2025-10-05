class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n = len(nums)
        firstDig = [int(str(x)[0]) for x in nums]
        lastDig = [x % 10 for x in nums]
        cnt = 0
        for i in range(n):
            for j in range(i + 1, n):
                if gcd(firstDig[i], lastDig[j]) == 1:
                    cnt += 1
        return cnt