class Solution {
public:
    int minFlips(int a, int b, int c) {
        int cnt = 0;
        while (a != 0 || b != 0 || c != 0)
        {
            int x = a & 1, y = b & 1, z = c & 1;
            if (x != y && z == 0)
                cnt++;
            else if (x == y && x == 1 && z == 0)
                cnt += 2;
            else if (x == y && x == 0 && z == 1)
                cnt++;
            a >>= 1;
            b >>= 1;
            c >>= 1;
        }
        return cnt;
    }
};