class Solution {
public:
    int balancedStringSplit(string s) {
        int c = 0, x = 0;
        for (char i : s)
        {
            if (i == 'L')
                x++;
            else
                x--;
            if (x == 0)
                c++;
        }
        return c;
    }
};