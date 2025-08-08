class Solution {
    unordered_map<int, unordered_map<int, double>> memo;
    double recurse(int a, int b) {
        if (a <= 0 && b <= 0)
            return 0.5;
        if (a <= 0)
            return 1.0;
        if (b <= 0)
            return 0.0;
        if (memo[a][b])
            return memo[a][b];
        return memo[a][b] = 0.25 * (recurse(a - 100, b) + recurse(a - 75, b - 25) + recurse(a - 50, b - 50) + recurse(a - 25, b - 75));
    }
public:
    double soupServings(int n) {
        if (n > 4800)
            return 1.0;
        return recurse(n, n);
    }
};