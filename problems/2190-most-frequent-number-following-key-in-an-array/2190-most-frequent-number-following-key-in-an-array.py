class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        f = Counter()
        for i in range(len(nums) - 1):
            if nums[i] == key:
                f[nums[i + 1]] += 1
        return max(f, key = f.get)