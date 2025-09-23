class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        l = [j for i in nums for j in i]
        c = Counter(l).items()
        return sorted([i for (i, j) in c if j == len(nums)])