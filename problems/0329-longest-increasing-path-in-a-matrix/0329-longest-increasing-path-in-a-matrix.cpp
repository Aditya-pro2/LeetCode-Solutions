class Solution {
public:
    int dfs(vector<vector<int>>& matrix, vector<vector<int>>& dp, vector<vector<bool>>& visited, int i, int j, int m, int n)
    {
        if (visited[i][j] == 0)
        {
            visited[i][j] = 1;
            if (i + 1 < m && matrix[i + 1][j] < matrix[i][j])
                dp[i][j] = max(dp[i][j], 1 + dfs(matrix, dp, visited, i + 1, j, m, n));
            if (j - 1 >= 0 && matrix[i][j - 1] < matrix[i][j])
                dp[i][j] = max(dp[i][j], 1 + dfs(matrix, dp, visited, i, j - 1, m, n));
            if (i - 1 >= 0 && matrix[i - 1][j] < matrix[i][j])
                dp[i][j] = max(dp[i][j], 1 + dfs(matrix, dp, visited, i - 1, j, m, n));
            if (j + 1 < n && matrix[i][j + 1] < matrix[i][j])
                dp[i][j] = max(dp[i][j], 1 + dfs(matrix, dp, visited, i, j + 1, m, n));
        }
        return dp[i][j];
    }

    int longestIncreasingPath(vector<vector<int>>& matrix)
    {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 1));
        vector<vector<bool>> visited(m, vector<bool>(n, 0));
        int ans = 1;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
            {
                dfs(matrix, dp, visited, i, j, m, n);
                ans = max(ans, dp[i][j]);
            }
        return ans;
    }
};