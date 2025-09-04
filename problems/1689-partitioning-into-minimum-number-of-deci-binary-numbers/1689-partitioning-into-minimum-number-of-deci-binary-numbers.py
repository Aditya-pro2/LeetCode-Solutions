class Solution:
    def minPartitions(self, n: str) -> int:
        n = str(n)
        for i in ["9", "8", "7", "6", "5", "4", "3", "2"]:
            if i in n:
                return int(i)
        return 1