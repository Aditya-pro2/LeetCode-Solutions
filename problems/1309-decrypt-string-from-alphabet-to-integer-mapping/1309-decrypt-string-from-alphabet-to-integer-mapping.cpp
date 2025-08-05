class Solution {
public:
    string freqAlphabets(string s) {
        int i = s.size() - 1;
        string t = "";
        while (i >= 0)
        {
            if (s[i] == '#')
            {
                int x = (s[i - 2] - '0') * 10 + (s[i - 1] - '0');
                t = char(x + 96) + t;
                i -= 3;
            }
            else
            {
                t = char(96 + (s[i] - '0')) + t;
                i--;
            }
        }
        return t;
    }
};