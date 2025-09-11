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
    int maxZigZag = 0;
    void dfs(TreeNode* node, bool isLeft, int length)
    {
        if (!node)
            return;
        maxZigZag = max(maxZigZag, length);
        if (isLeft)
        {
            dfs(node->left, false, length + 1);
            dfs(node->right, true, 1);
        }
        else
        {
            dfs(node->right, true, length + 1);
            dfs(node->left, false, 1);
        }
    }
public:
    int longestZigZag(TreeNode* root)
    {
        dfs(root, true, 0);
        dfs(root, false, 0);
        return maxZigZag;
    }
};