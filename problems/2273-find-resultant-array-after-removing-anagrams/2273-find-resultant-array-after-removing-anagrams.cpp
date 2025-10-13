class Solution {
public:
    vector<string> removeAnagrams(vector<string>& words) {
        vector<string> ans;
        ans.push_back(words[0]);
        for (int i = 1; i < words.size(); i++)
        {
            string a = ans.back(), b = words[i];
            string x = a, y = b;
            sort(x.begin(), x.end());
            sort(y.begin(), y.end());
            if (x != y)
                ans.push_back(b);
        }
        return ans;
    }
};