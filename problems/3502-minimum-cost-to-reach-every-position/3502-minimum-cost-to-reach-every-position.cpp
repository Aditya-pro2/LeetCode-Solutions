class Solution {
public:
    vector<int> minCosts(vector<int>& cost) {
        int m = cost[0];
        for (int i = 1; i < cost.size(); i++)
        {
            m = min(m, cost[i]);
            cost[i] = m;
        }
        return cost;
    }
};