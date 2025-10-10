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
    int x = 0;
    pair<int, int> fun(TreeNode* root) {
        if (!root)
            return {0, 0};
        pair<int, int> l = fun(root->left), r = fun(root->right);
        int s = root->val + l.first + r.first, c = 1 + l.second + r.second;
        if (root->val == s / c)
            x++;
        return {s, c};
    }
public:
    int averageOfSubtree(TreeNode* root) {
        fun(root);
        return x;
    }
};