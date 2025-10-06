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
    int fun(TreeNode* root, int x)
    {
        if (!root)
            return -1;
        if (root->val > x)
            return root->val;
        int l = fun(root->left, x);
        int r = fun(root->right, x);
        if (l != -1 && r != -1)
            return min(l, r);
        return l != -1 ? l : r;
    }
public:
    int findSecondMinimumValue(TreeNode* root) {
        return fun(root, root->val);
    }
};