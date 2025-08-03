class Solution {
    int find(vector<int>& root, int i)
    {
        return (i == root[i]) ? i : find(root, root[i]);
    }
public:
    int minSwapsCouples(vector<int>& row) {
        int n = row.size(), ans = 0;
        vector<int> root(n);
        for (int i = 0; i < n; i++)
            root[i] = i;
        for (int i = 0; i < n; i += 2)
        {
            int x = find(root, row[i] / 2), y = find(root, row[i + 1] / 2);
            if (x == y)
                continue;
            root[x] = y;
            ans++;
        }
        return ans;
    }
};