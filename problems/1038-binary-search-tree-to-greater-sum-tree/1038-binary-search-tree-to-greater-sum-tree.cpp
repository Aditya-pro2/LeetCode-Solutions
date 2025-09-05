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
public:
    TreeNode* bstToGst(TreeNode* root) {
        if (root->right)
            bstToGst(root->right);
        x = root->val = x + root->val;
        if (root->left)
            bstToGst(root->left);
        return root;
    }
};