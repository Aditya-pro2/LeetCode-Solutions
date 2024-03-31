class Solution {
public:
    int findPoisonedDuration(vector<int>& t, int d) {
        int c = 0;
        for (int i = 0; i < t.size() - 1; i++)
            c += (t[i + 1] - t[i] >= d) ? d : t[i + 1] - t[i];
        return c + d;
    }
};