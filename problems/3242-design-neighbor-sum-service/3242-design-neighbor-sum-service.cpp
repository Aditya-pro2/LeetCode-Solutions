class NeighborSum {
    vector<vector<int>> a;
    int n;
public:
    NeighborSum(vector<vector<int>>& grid) {
        a = grid;
        n = grid.size();
    }
    
    int adjacentSum(int value) {
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (a[i][j] == value)
                {
                    int l = (j > 0) ? a[i][j - 1] : 0;
                    int r = (j < a[i].size() - 1) ? a[i][j + 1] : 0;
                    int u = (i > 0) ? a[i - 1][j] : 0;
                    int d = (i < n - 1) ? a[i + 1][j] : 0;
                    return l + r + u + d;
                }
        return -1;
    }
    
    int diagonalSum(int value) {
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (a[i][j] == value)
                {
                    int s = 0;
                    if (i >= 1 && j >= 1)
                        s += a[i - 1][j - 1];
                    if (i < n - 1 && j < n - 1)
                        s += a[i + 1][j + 1];
                    if (i < n - 1 && j >= 1)
                        s += a[i + 1][j - 1];
                    if (i >= 1 && j < n - 1)
                        s += a[i - 1][j + 1];
                    return s;
                }
        return -1;
    }
};

/**
 * Your NeighborSum object will be instantiated and called as such:
 * NeighborSum* obj = new NeighborSum(grid);
 * int param_1 = obj->adjacentSum(value);
 * int param_2 = obj->diagonalSum(value);
 */