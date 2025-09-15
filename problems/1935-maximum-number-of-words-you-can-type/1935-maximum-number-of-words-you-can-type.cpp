class Solution {
public:
    int canBeTypedWords(string text, string broken) {
        int m = 0, c = 0, wm = 0;
        for (int i = 0; i < broken.size(); i++)
            m |= 1 << (broken[i] - 97);
        for (int i = 0; i <= text.size(); i++)
        {
            if (i < text.size() && text[i] >= 'a' && text[i] <= 'z')
                wm |= m & (1 << (text[i] - 97));
            if (i == text.size() || text[i] == ' ')
            {
                if (wm == 0)
                    c++;
                wm = 0;
            }
        }
        return c;
    }
};