class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        nums2, indices, result = sorted([(nums[i], i) for i in range(n)]), [], [0] * n
        for i in range(n):
            if i == 0 or nums2[i][0] - nums2[i - 1][0] > limit:
                indices.append([])
            indices[-1].append(nums2[i][1])
        for index in indices: # index is one set of sortable numbers
            sortedIndex = sorted(index)
            for j in range(len(index)):
                result[sortedIndex[j]] = nums[index[j]]
        return result