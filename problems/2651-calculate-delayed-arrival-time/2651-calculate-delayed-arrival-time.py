class Solution:
    def findDelayedArrivalTime(self, a: int, d: int) -> int:
        return (a + d) % 24