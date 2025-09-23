class Solution {
public:
    string reverseOnlyLetters(string s) {
        int n = s.size(), a = 0, b = n - 1;
        while(a < b)
        {
            if (isalpha(s[a]) && isalpha(s[b]))
                swap(s[a++], s[b--]);
            else if (!isalpha(s[a]))
                a++;
            else
                b--;
        }
        return s;
    }
};