class Solution {
public:
    // Helper function to determine the next diagonal direction
    int getNext(int d) {
        if (d == 0) return 3; // ↖ (top-left) -> ↗ (top-right) 
        if (d == 1) return 2; // ↘ (bottom-right) -> ↙ (bottom-left)
        if (d == 2) return 0; // ↙ (bottom-left) -> ↖ (top-left)
        return 1;             // ↗ (top-right) -> ↘ (bottom-right)
    }
    
    // Helper function to determine the current diagonal direction
    int getCurr(int d) {
        if (d == 0) return 1; // ↖ (top-left) -> ↘ (bottom-right)
        if (d == 1) return 0; // ↘ (bottom-right) -> ↖ (top-left)
        if (d == 2) return 3; // ↙ (bottom-left) -> ↗ (top-right)
        return 2;             // ↗ (top-right) -> ↙ (bottom-left)
    }
    
    int lenOfVDiagonal(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        // DP array to store diagonal lengths in four directions
        vector<vector<array<int, 4>>> dp(n, vector<array<int, 4>>(m, {0, 0, 0, 0}));
        
        // Directions for diagonal traversal: ↖, ↘, ↙, ↗
        vector<pair<int, int>> dirs = {{-1,-1}, {1,1}, {1,-1}, {-1,1}};

        // Compute DP values for ↖ (top-left to bottom-right)
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                if (grid[i][j] != 1 && grid[i - 1][j - 1] != 1 && grid[i - 1][j - 1] != grid[i][j]) {
                    dp[i][j][0] = dp[i - 1][j - 1][0] + 1;
                }
            }
        }

        // Compute DP values for ↘ (bottom-right to top-left)
        for (int i = n - 2; i >= 0; i--) {
            for (int j = m - 2; j >= 0; j--) {
                if (grid[i][j] != 1 && grid[i + 1][j + 1] != 1 && grid[i + 1][j + 1] != grid[i][j]) {
                    dp[i][j][1] = dp[i + 1][j + 1][1] + 1;
                }
            }
        }

        // Compute DP values for ↙ (bottom-left to top-right)
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 1; j < m; j++) {
                if (grid[i][j] != 1 && grid[i + 1][j - 1] != 1 && grid[i + 1][j - 1] != grid[i][j]) {
                    dp[i][j][2] = dp[i + 1][j - 1][2] + 1;
                }
            }
        }

        // Compute DP values for ↗ (top-right to bottom-left)
        for (int i = 1; i < n; i++) {
            for (int j = m - 2; j >= 0; j--) {
                if (grid[i][j] != 1 && grid[i - 1][j + 1] != 1 && grid[i - 1][j + 1] != grid[i][j]) {
                    dp[i][j][3] = dp[i - 1][j + 1][3] + 1;
                }
            }
        }

        int maxV = 0; // Maximum valid diagonal length
        
        // Iterate over each cell in the grid
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] != 1) continue; // Skip cells that are not 1
                maxV = max(maxV, 1);

                // Check diagonal connections
                for (int d = 0; d < 4; d++) {
                    int nextDir = getNext(d); // the next possible dir which is in clockwise direction.
                    int currDir = getCurr(d); // the current dir which is opposite to d since we see from the other side to 1.
                    auto& dir = dirs[d];

                    int ci = i + dir.first, cj = j + dir.second;
                    if (ci < 0 || cj < 0 || ci >= n || cj >= m || grid[ci][cj] != 2) continue;

                    // Expand along the diagonal while conditions are met
                    while (ci >= 0 && cj >= 0 && ci < n && cj < m && grid[ci][cj] != grid[ci-dir.first][cj-dir.second] && grid[ci][cj] != 1) {
                        maxV = max(maxV, dp[ci][cj][nextDir] + dp[ci][cj][currDir] + 2);
                        // We can get off by not checking a straight diagonal since it will come under this case as well due to the while loop.
                        ci += dir.first;
                        cj += dir.second;
                    }
                }                
            }
        }

        return maxV; // Return the maximum diagonal length found
    }
};