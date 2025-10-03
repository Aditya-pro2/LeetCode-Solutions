class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        common, m1, m2 = set(nums1).intersection(nums2), min(nums1), min(nums2)
        return min(common) if common else min(m1, m2) * 10 + max(m1, m2)