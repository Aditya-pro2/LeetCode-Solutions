class Solution {
public:
    int countTestedDevices(vector<int>& b) {
        int x = 0, n = b.size();
        for(int i = 0; i < n; i++)
        {
            b[i] = max(0, b[i] - x);
            if (b[i] > 0)
                x += 1;
        }
        return x;
    }
};