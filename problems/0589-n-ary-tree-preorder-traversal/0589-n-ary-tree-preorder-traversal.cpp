/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    vector<int> a;
    void fun(Node* root)
    {
        if (!root)
            return;
        a.push_back(root->val);
        for (auto i : root->children)
            fun(i);
    }
public:
    vector<int> preorder(Node* root)
    {
        a.clear();
        fun(root);
        return a;
    }
};