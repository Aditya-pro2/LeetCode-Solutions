class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        x = (sum(aliceSizes) - sum(bobSizes)) / 2
        aliceSizes = set(aliceSizes)
        for b in set(bobSizes):
            if x + b in aliceSizes:
                return [x + b, b]