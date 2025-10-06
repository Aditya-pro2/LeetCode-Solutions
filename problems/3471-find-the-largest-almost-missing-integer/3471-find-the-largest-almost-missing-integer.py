class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        c = defaultdict(int)
        for i in range(0, len(nums) - (k - 1)):
            for v in set(nums[i : i + k]):
                c[v] += 1
        value = -1
        for key in c:
            if c[key] == 1:
                value = max(value, key)
        return value