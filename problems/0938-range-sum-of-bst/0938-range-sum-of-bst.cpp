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
public:
    void sum(TreeNode* root, int low, int high, int &s)
    {
        if (!root)
            return;
        if (low <= root->val && root->val <= high)
        {
            sum(root->left, low, high, s);
            s += root->val;
            sum(root->right, low, high, s);
        }
        else if (root->val < low)
            sum(root->right, low, high, s);
        else
            sum(root->left, low, high, s);
    }
    int rangeSumBST(TreeNode* root, int low, int high) {
        int s = 0;
        sum(root, low, high, s);
        return s;
    }
};