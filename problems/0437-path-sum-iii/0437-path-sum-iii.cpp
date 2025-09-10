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
#define ll long long
    int solve(TreeNode* root, ll target, ll sum, unordered_map<ll, ll>& mpp)
    {
        if (root == nullptr)
            return 0;
        sum += (ll)root->val;
        int cnt = mpp[sum - target];
        mpp[sum]++;
        cnt += solve(root->left, target, sum, mpp);
        cnt += solve(root->right, target, sum, mpp);
        mpp[sum]--;
        if (mpp[sum] == 0)
            mpp.erase(sum);
        return cnt;
    }
public:
    int pathSum(TreeNode* root, int targetSum) {
        unordered_map<ll, ll> mpp;
        mpp[0] = 1;
        return solve(root, (ll)targetSum, 0LL, mpp);
    }
};