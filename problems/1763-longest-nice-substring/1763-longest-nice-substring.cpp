class Solution {
public:
    string longestNiceSubstring(string s) {
        int n = s.size();
        if (n < 2)
            return "";
        for (int i = 0; i < n; i++)
        {
            char ch = s[i];
            bool nice = false;
            for (int j = 0; j < n; j++)
            {
                char ch1 = s[j];
                if ((isupper(ch) && ch1 == tolower(ch)) || (islower(ch) && ch1 == toupper(ch)))
                {
                    nice = true;
                    break;
                }
            }
            if (!nice)
            {
                string left = longestNiceSubstring(s.substr(0, i));
                string right = longestNiceSubstring(s.substr(i + 1));
                return (left.size() >= right.size() ? left : right);
            }
        }
        return s;
    }
};