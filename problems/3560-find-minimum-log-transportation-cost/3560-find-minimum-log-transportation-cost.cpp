class Solution {
public:
    long long minCuttingCost(int n, int m, int k) {
        long long c = 0;
        if (n > k)
            c += 1LL * k * (n - k);
        if (m > k)
            c += 1LL * k * (m - k);
        return c;
    }
};