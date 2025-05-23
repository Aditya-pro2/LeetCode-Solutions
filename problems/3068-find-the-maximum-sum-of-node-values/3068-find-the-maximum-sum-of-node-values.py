class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        total_no, total_yes = nums[0], nums[0]^k
        for n in nums[1:]:
            total_no, total_yes = (max(n + total_no, (n^k) + total_yes), 
                                   max((n^k) + total_no, n + total_yes))
        return total_no