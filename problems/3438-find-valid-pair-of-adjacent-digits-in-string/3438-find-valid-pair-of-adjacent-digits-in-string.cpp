class Solution {
public:
    string findValidPair(string s) {
        int n = s.size();
        priority_queue<pair<int, int>> pq;
        vector<int> d(10, 0), f(10, -1);
        for (int i = 0; i < n; i++)
            d[s[i] - '0']++;
        for (int i = 0; i < n - 1; i++)
        {
            string temp = "";
            temp += s[i];
            temp += s[i + 1];
            if (s[i] == s[i + 1])
                continue;
            if (d[s[i] - '0'] == s[i] - '0' && d[s[i + 1] - '0'] == s[i + 1] - '0')
                return temp;
        }
        return "";
    }
};