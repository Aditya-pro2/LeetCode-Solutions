class Solution {
    void dfs(int u, vector<vector<int>>& isConnected, vector<bool>& vis)
    {
        for (int v = 0; v < isConnected.size(); v++)
        {
            if (isConnected[u][v] == 1 && (!vis[v]))
            {
                vis[v] = true;
                dfs(v, isConnected, vis);
            }
        }
    }
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int V = isConnected.size(), c = 0;
        vector<bool> vis(V, false);
        for (int i = 0; i < V; i++)
        {
            if (!vis[i])
            {
                vis[i] = true;
                dfs(i, isConnected, vis);
                c++;
            }
        }
        return c;
    }
};