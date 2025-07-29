class Solution {
public:
    string reversePrefix(string word, char ch) {
        string t = "";
        bool x = false;
        for (char i : word)
        {
            if (x)
                t += i;
            else
                t = i + t;
            if (i == ch)
                x = true;
        }
        if (x)
            return t;
        return word;
    }
};