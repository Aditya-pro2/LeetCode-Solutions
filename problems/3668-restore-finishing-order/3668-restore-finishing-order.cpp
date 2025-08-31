class Solution {
public:
    vector<int> recoverOrder(vector<int>& order, vector<int>& friends) {
        int n = order.size();
        vector<bool> x(n, false);
        vector<int> l;
        for (int i = 0; i < friends.size(); i++)
            x[friends[i] - 1] = true;
        for (int i = 0; i < n; i++)
            if (x[order[i] - 1])
                l.push_back(order[i]);
        return l;
    }
};