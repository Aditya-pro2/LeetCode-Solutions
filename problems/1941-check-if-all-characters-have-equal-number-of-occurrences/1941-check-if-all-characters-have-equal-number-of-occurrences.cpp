class Solution {
public:
    bool areOccurrencesEqual(string s) {
        unordered_map<char, int> m;
        for (int i = 0; i < s.size(); i++)
            m[s[i]]++;
        unordered_set<int> set;
        for (auto i : m)
            set.insert(i.second);
        return set.size() == 1;
    }
};