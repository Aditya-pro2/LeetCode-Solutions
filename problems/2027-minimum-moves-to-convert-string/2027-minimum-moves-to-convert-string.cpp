class Solution {
public:
    int minimumMoves(string s) {
        int i = 0, c = 0;
        while (i < s.size())
        {
            if (s[i] == 'X')
            {
                c++;
                i += 3;
            }
            else
                i++;
        }
        return c;
    }
};