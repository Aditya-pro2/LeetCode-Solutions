class Solution {
public:
    int buttonWithLongestTime(vector<vector<int>>& events) {
        int m = events[0][1], ans = events[0][0];
        for (int i = 1; i < events.size(); i++)
        {
            int x = events[i][1] - events[i - 1][1];
            if (x > m || (x == m && events[i][0] < ans))
            {
                m = x;
                ans = events[i][0];
            }
        }
        return ans;
    }
};