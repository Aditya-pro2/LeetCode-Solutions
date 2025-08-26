class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int x = 0;
        for (auto i : accounts)
        {
            int y = 0;
            for (auto j : i)
                y += j;
            if (x < y)
                x = y;
        }
        return x;
    }
};