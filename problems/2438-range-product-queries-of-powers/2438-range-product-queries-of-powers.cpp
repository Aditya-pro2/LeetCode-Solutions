class Solution {
public:
    vector<int> productQueries(int n, vector<vector<int>>& queries) {
        int mod = 1000000007, x = 1, m = queries.size();
        vector<long long> b;
        while (n > 0)
        {
            if (n & 1)
                b.push_back(x);
            n >>= 1;
            x <<= 1;
        }
        int l = b.size();
        vector<vector<long long>> res(l, vector<long long>(l));
        for (int i = 0; i < l; i++)
        {
            long long curr = 1;
            for (int j = i; j < l; j++)
            {
                curr = (curr * b[j]) % mod;
                res[i][j] = curr;
            }
        }
        vector<int> ans(m);
        for (int i = 0; i < m; i++)
            ans[i] = (int)res[queries[i][0]][queries[i][1]];
        return ans;
    }
};