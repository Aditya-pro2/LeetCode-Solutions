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
    int sumRootToLeaf(TreeNode* root, int s = 0) {
        if (!root)
            return 0;
        s = 2 * s + root->val;
        if ((!root->left) && (!root->right))
            return s;
        return sumRootToLeaf(root->left, s) + sumRootToLeaf(root->right, s);
    }
};