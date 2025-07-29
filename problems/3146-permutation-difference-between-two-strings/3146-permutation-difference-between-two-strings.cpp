class Solution {
public:
    int findPermutationDifference(string s, string t) {
        int c = 0;
        unordered_map<char, pair<int, int>> m;
        for (int i = 0; i < s.size(); i++)
            m[s[i]].first = i;
        for (int i = 0; i < t.size(); i++)
            m[t[i]].second = i;
        for (auto i : m)
            c += abs(i.second.first - i.second.second);
        return c;
    }
};