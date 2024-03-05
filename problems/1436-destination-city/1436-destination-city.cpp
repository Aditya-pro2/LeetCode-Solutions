class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_set<string> x;
        for (const auto& i : paths)
            x.insert(i[0]);
        for (const auto& i : paths)
        {
            const std::string& y = i[1];
            if (x.find(y) == x.end())
                return y;
        }
        return "";
    }
};