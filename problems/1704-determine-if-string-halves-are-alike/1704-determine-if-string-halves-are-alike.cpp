class Solution {
    int vowel(string s, int i, int j)
    {
        int c = 0;
        for (int k = i; k < j; k++)
            if (s[k] == 'a' || s[k] == 'e' || s[k] == 'i' || s[k] == 'o' || s[k] == 'u')
                c++;
        return c;
    }
public:
    bool halvesAreAlike(string s) {
        int n = s.size();
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        return vowel(s, 0, n / 2) == vowel(s, n / 2, n);
    }
};