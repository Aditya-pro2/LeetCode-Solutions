class Solution {
public:
    bool canAliceWin(int n) {
        int x = 10, y = 1;
        while (n >= x)
        {
            n -= x;
            y = x & 1;
            x--;
        }
        return y == 0;
    }
};