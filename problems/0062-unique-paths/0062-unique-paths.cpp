class Solution {
public:
    int uniquePaths(int m, int n)
    {
        long long curr = 1;
        for (int i = 1; i <= m - 1; i++)
            curr = curr * (n + i - 1) / i;
        return (int)curr;
    }
};