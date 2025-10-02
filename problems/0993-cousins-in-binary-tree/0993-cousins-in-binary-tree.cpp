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
    TreeNode* findNode(TreeNode* node, int x) {
        if (!node)
            return NULL;
        if (node->val == x)
            return node;
        TreeNode* l = findNode(node->left, x);
        if (l)
            return l;
        return findNode(node->right, x);
    }

    int level(TreeNode* node, TreeNode* target, int lev) {
        if (!node)
            return 0;
        if (node == target)
            return lev;
        int l = level(node->left, target, lev + 1);
        if (l)
            return l;
        return level(node->right, target, lev + 1);
    }

    bool isSibling(TreeNode* node, TreeNode* x, TreeNode* y) {
        if (!node)
            return false;
        return ((node->left == x && node->right == y) || (node->left == y && node->right == x) || isSibling(node->left, x, y) || isSibling(node->right, x, y));
    }

public:
    bool isCousins(TreeNode* root, int x, int y) {
        TreeNode* xx = findNode(root, x);
        TreeNode* yy = findNode(root, y);
        return (level(root, xx, 0) == level(root, yy, 0)) && (!isSibling(root, xx, yy));
    }
};