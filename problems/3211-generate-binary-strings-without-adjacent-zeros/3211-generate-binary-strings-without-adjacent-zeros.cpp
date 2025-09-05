class Solution {
    void back(vector<string>& ans, string x, int n)
    {
        if (x.size() == n)
        {
            ans.push_back(x);
            return;
        }
        back(ans, x + "1", n);
        if (x.size() == 0 || x[x.size() - 1] != '0')
            back(ans, x + "0", n);
    }
public:
    vector<string> validStrings(int n) {
        vector<string> ans;
        back(ans, "", n);
        return ans;
    }
};