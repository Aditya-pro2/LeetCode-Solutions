class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        x = max(candies)
        l = [x - i <= extraCandies for i in candies]
        return l