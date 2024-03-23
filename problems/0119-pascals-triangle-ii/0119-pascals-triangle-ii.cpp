class Solution {
public:
    vector<int> getRow(int x) {
        vector<int>v;
        for (int i = 0; i <= x; i++)
        {
            long long y = 1;
            for (int j = 0; j <= i; j++)
            {
                if (i == x)
                    v.push_back(y);
                y = y * (i - j) / (j + 1);
            }
        }
        return v;
    }
};