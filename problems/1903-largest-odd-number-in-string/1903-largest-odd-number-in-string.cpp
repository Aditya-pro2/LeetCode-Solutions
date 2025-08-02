class Solution {
public:
    string largestOddNumber(string num) {
        int n = num.size();
        for (int i = n; i >= 1; i--)
            if (int(num[i - 1]) & 1)
                return num.substr(0, i);
        return "";
    }
};