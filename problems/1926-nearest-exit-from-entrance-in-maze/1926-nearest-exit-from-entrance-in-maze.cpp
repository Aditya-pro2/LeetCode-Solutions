class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        int n = maze.size();
        int m = maze[0].size();
        vector<vector<int>> vis(n, vector<int>(m, 0));
        queue<tuple<int, int, int>> q;
        q.push({entrance[0], entrance[1], 0});
        vis[entrance[0]][entrance[1]] = 2;
        while (!q.empty())
        {
            auto [row, col, step] = q.front();
            q.pop();
            if ((row == n - 1 || row == 0 || col == m - 1 || col == 0) && vis[row][col] != 2)
                return step;
            int dr[4] = {1, 0, -1, 0};
            int dc[4] = {0, -1, 0, 1};
            for (int i = 0; i < 4; i++)
            {
                int nr = row + dr[i];
                int nc = col + dc[i];
                if (nr >= 0 && nr < n && nc >= 0 && nc < m && maze[nr][nc] == '.' && !vis[nr][nc])
                {
                    q.push({nr, nc, step + 1});
                    vis[nr][nc] = 1;
                }
            }
        }
        return -1;
    }
};