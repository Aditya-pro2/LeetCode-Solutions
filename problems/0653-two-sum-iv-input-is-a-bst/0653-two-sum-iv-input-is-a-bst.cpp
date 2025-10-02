/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
    void inorder(TreeNode* node, vector<int>& nums) {
        if (!node)
            return;
        inorder(node->left, nums);
        nums.push_back(node->val);
        inorder(node->right, nums);
    }
public:
    bool findTarget(TreeNode* root, int k) {
        vector<int> nums;
        inorder(root, nums);
        int l = 0;
        int r = nums.size() - 1;
        while (l < r)
        {
            if (nums[l] + nums[r] == k)
                return true;
            if (nums[l] + nums[r] < k)
                l++;
            if (nums[l] + nums[r] > k)
                r--;
        }
        return false;
    }
};