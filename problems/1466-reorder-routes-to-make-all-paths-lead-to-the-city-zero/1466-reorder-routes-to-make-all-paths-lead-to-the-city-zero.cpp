class Solution {
    int helper(vector<vector<int>>& connections, vector<bool>& vis, vector<vector<int>>& idx, int u)
    {
        int x = 0;
        for (auto i : idx[u])
        {
            if (vis[i])
                continue;
            vis[i] = true;
            if (connections[i][0] == u)
                x += (helper(connections, vis, idx, connections[i][1]) + 1);
            else if (connections[i][1] == u)
                x += helper(connections, vis, idx, connections[i][0]);
            vis[i] = false;
        }
        return x;
    }
public:
    int minReorder(int n, vector<vector<int>>& connections) {
        vector<bool> vis(n);
        vector<vector<int>> idx(n);
        for (int i = 0; i < connections.size(); i++)
        {
            idx[connections[i][0]].emplace_back(i);
            idx[connections[i][1]].emplace_back(i);
        }
        return helper(connections, vis, idx, 0);
    }
};