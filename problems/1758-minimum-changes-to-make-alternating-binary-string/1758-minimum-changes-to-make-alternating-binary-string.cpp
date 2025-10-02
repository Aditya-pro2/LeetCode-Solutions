class Solution {
public:
    int minOperations(string s) {
        int n = s.size(), x = 0;
        for (int i = 0; i < n; i++)
            x += ((i & 1) == (s[i] & 1));
        return min(x, n - x);
    }
};