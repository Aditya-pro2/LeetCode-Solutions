/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    int ans = INT_MAX, x = -1;
    void fun(TreeNode* root)
    {
        if (!root)
            return;
        fun(root->left);
        if (x != -1)
            ans = min(ans, root->val - x);
        x = root->val;
        fun(root->right);
    }
public:
    int minDiffInBST(TreeNode* root) {
        fun(root);
        return ans;
    }
};