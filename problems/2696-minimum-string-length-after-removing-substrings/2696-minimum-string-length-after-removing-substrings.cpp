class Solution {
public:
    int minLength(string s) {
        int n = s.size();
        if (n < 2)
            return n;
        int x = 1;
        for (int i = 1; i < n; i++)
        {
            s[x] = s[i];
            if (x > 0 && ((s[x - 1] == 'A' && s[i] == 'B') || (s[x - 1] == 'C' && s[i] == 'D')))
                x--;
            else
                x++;
        }
        return x;
    }
};