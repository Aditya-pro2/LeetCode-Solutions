class Solution {
public:
    int reverseDegree(string s) {
        int c = 0;
        for (int i = 0; i < s.size(); i++)
            c += ((i + 1) * (123 - s[i]));
        return c;
    }
};