class Solution {
    long long fun(int n)
    {
        if (n == 0)
            return 1;
        if (n & (n - 1) == 0)
            return n << 1;
        return 1 << (32 - __builtin_clz(n));
    }
public:
    int bitwiseComplement(int n) {
        if (n == 0)
            return 1;
        long long x = fun(n);
        return x - n - 1;
    }
};