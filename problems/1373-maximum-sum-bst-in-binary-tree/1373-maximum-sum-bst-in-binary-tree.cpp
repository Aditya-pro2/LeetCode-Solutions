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
class Node
{
public:
    int min, max, sum;

    Node(int a, int b, int c)
    {
        min = a;
        max = b;
        sum = c;
    }
};

class Solution {
    int ans = 0;
    Node helper(TreeNode* root)
    {
        if (!root)
            return Node(INT_MAX, INT_MIN, 0);
        Node l = helper(root->left);
        Node r = helper(root->right);
        if (root->val > l.max && root->val < r.min)
        {
            ans = max(ans, root->val + l.sum + r.sum);
            return Node(min(root->val, l.min), max(root->val, r.max), root->val + l.sum + r.sum);
        }
        return Node(INT_MIN, INT_MAX, max(l.sum, r.sum));
    }
public:
    int maxSumBST(TreeNode* root) {
        helper(root);
        return ans;
    }
};