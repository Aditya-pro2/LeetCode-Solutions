class Solution {
public:
    int minimumOperations(vector<vector<int>>& grid) {
        const int r = grid.size(), c = grid[0].size();
        int cnt = 0;
        for (int i = 1; i < r; i++)
        {
            auto& row = grid[i];
            for (int j = 0; j < c; j++)
            {
                int x = max(row[j], grid[i - 1][j] + 1);
                cnt += (x - row[j]);
                row[j] = x;
            }
        }
        return cnt;
    }
};