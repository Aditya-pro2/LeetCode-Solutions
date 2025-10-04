class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = Counter(x for x in nums if x % 2 == 0)
        if not freq:
            return -1
        m = max(freq.values())
        res = min(x for x, v in freq.items() if v == m)
        return res