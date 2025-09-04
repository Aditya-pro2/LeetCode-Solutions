class Solution {
public:
    int countCompleteDayPairs(vector<int>& hours) {
        vector<int> t(25, 0);
        int c = 0;
        for (int x : hours)
        {
            if (x % 24 == 0)
            {
                c += t[24];
                t[24]++;
            }
            else
            {
                c += t[24 - (x % 24)];
                t[x % 24]++;
            }
        }
        return c;
    }
};