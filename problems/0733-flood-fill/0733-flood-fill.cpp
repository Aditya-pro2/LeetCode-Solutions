class Solution {
public:
    void dfs(int r, int c, int m, int n, vector<vector<int>>& image, vector<vector<bool>>& vis, int newColor, int oldColor)
    {
        vis[r][c] = true;
        image[r][c] = newColor;
        if (r >= 1 && !vis[r - 1][c] && image[r - 1][c] == oldColor)
            dfs(r - 1, c, m, n ,image, vis, newColor, oldColor);
        if (r < m - 1 && !vis[r + 1][c] && image[r + 1][c] == oldColor)
            dfs(r + 1, c, m, n ,image, vis, newColor, oldColor);
        if (c >= 1 && !vis[r][c - 1] && image[r][c - 1] == oldColor)
            dfs(r, c - 1, m, n ,image, vis, newColor, oldColor);
        if (c < n - 1 && !vis[r][c + 1] && image[r][c + 1] == oldColor)
            dfs(r, c + 1, m, n ,image, vis, newColor, oldColor);
    }

    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color)
    {
        int m = image.size(), n = image[0].size();
        vector<vector<bool>> vis(m, vector<bool>(n, false));
        dfs(sr, sc, m, n ,image, vis, color, image[sr][sc]);
        return image;
    }
};