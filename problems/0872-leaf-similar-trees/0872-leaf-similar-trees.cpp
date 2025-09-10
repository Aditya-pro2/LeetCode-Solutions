class Solution {
    void preOrder1(TreeNode* temp,vector<int>& arr)
    {
        if(!temp)
            return;
        if((!temp->left) && (!temp->right))
            arr.push_back(temp->val);
        preOrder1(temp->left,arr);
        preOrder1(temp->right,arr);
    }
public:
    bool leafSimilar(TreeNode* root1, TreeNode* root2)
    {
        vector<int> arr1,arr2;
        preOrder1(root1,arr1);
        preOrder1(root2,arr2);
        return arr1 == arr2;
    }
};