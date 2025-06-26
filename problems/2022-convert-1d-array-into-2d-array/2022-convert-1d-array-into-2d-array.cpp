class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
        int N = original.size();
        if (N != (m * n))
            return {};
        vector<vector<int>> newArray(m, vector<int> (n));
        int x = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                newArray[i][j] = original[x++];
        return newArray;
    }
};