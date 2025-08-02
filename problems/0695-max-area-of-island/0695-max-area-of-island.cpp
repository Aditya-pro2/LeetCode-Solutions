class Solution {
public:
    vector<int> dx = {-1, 0, 1, 0};
    vector<int> dy = {0, 1, 0, -1};
    void dfs(int i, int j, int& count, vector<vector<int>>& grid, vector<vector<int>>& vis)
    {
        int n = grid.size();
        int m = grid[0].size();
        count++;
        vis[i][j] = 1;
        for (int k = 0; k < 4; k++)
        {
            int x = dx[k] + i;
            int y = dy[k] + j;
            if (x >= 0 && x < n && y >= 0 && y < m && !vis[x][y] && grid[x][y] == 1)
                dfs(x, y, count, grid, vis);
        }
    }
    int maxAreaOfIsland(vector<vector<int>>& grid)
    {
        int n = grid.size(), m = grid[0].size(), max_area = 0;
        vector<vector<int>> vis(n, vector<int>(m, 0));
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (!vis[i][j] && grid[i][j] == 1)
                {
                    int count = 0;
                    dfs(i, j, count, grid, vis);
                    max_area = max(max_area, count);
                }
        return max_area;
    }
};