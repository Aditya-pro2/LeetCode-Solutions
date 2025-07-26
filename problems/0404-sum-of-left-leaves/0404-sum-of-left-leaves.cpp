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
    void helper(TreeNode* root, bool l, int& s)
    {
        if (!root)
            return;
        if (!(root->left || root->right) && l)
            s += root->val;
        helper(root->left, true, s);
        helper(root->right, false, s);
    }
public:
    int sumOfLeftLeaves(TreeNode* root) {
        int s = 0;
        helper(root, false, s);
        return s;
    }
};