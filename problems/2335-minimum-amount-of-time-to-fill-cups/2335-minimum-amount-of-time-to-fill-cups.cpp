class Solution {
public:
    int fillCups(vector<int>& amount) {
        sort(amount.begin(), amount.end());
        int x = amount[0], y = amount[1], z = amount[2];
        int s = x + y + z;
        if (x + y > z)
            return (s / 2) + (s % 2);
        return z;
    }
};