# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        x = max(nums)
        i = nums.index(x)        
        n = TreeNode(x)
        n.left = self.constructMaximumBinaryTree(nums[0 : i])
        n.right = self.constructMaximumBinaryTree(nums[(i + 1):])
        return n